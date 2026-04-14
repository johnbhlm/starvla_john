# Copyright 2025 starVLA community. All rights reserved.
# Licensed under the MIT License, Version 1.0 (the "License"); 
# Implemented by [Jinhui YE / HKUST University] in [2025].


"""
StarVLA’s trainer is built directly on native PyTorch + Accelerate + DeepSpeed, keeping the loop explicit and easy to hack.
Conventions:
1. Store runtime state in dicts where possible (simplifies data info, procesing info, config, etc).  
2. Use multiple dataloaders to adapt heterogeneous data types / task mixtures.  
3. Put each training strategy in its own `trainer_*.py` file (avoid large if‑else chains).  
"""

# Standard Library
import argparse
import json
import os
from pathlib import Path
from typing import Tuple
from torch.utils.data import DataLoader
import numpy as np
import time
import subprocess
import threading

# Third-Party Libraries
import torch
import torch.distributed as dist
import wandb
# os.environ["WANDB_DISABLED"] = "true"
# os.environ["WANDB_MODE"] = "disabled"
import yaml
from accelerate import Accelerator, DeepSpeedPlugin
from accelerate.logging import get_logger
from accelerate.utils import set_seed
from omegaconf import OmegaConf
from tqdm import tqdm
from transformers import AutoProcessor, get_scheduler

# Local Modules
from starVLA.dataloader import build_dataloader
from starVLA.training.trainer_utils.trainer_tools import normalize_dotlist_args
from starVLA.model.framework import build_framework
from starVLA.training.trainer_utils.trainer_tools import TrainerUtils
from starVLA.training.trainer_utils.trainer_tools import build_param_lr_groups
from starVLA.training.trainer_utils.config_tracker import wrap_config, AccessTrackedConfig

deepspeed_plugin = DeepSpeedPlugin()
accelerator = Accelerator(deepspeed_plugin=deepspeed_plugin)
accelerator.print(accelerator.state)

# Sane Defaults
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import warnings
warnings.filterwarnings("ignore", message=".*video decoding and encoding capabilities.*")
warnings.filterwarnings("ignore", category=UserWarning, module="torchvision")

# Initialize Overwatch =>> Wraps `logging.Logger`
logger = get_logger(__name__)


def load_fast_tokenizer():
    fast_tokenizer = AutoProcessor.from_pretrained("physical-intelligence/fast", trust_remote_code=True)
    return fast_tokenizer


def setup_directories(cfg) -> Path:
    """create output directory and save config"""
    cfg.output_dir = os.path.join(cfg.run_root_dir, cfg.run_id)
    output_dir = Path(cfg.output_dir)

    if not dist.is_initialized() or dist.get_rank() == 0:
        # create output directory and checkpoint directory
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(output_dir / "checkpoints", exist_ok=True)

        # # save config
        # OmegaConf.save(cfg, output_dir / "config.yaml")
        # with open(output_dir / "config.yaml", "r") as f_yaml, open(output_dir / "config.json", "w") as f_json:
        #     yaml_cfg = yaml.safe_load(f_yaml)
        #     json.dump(yaml_cfg, f_json, indent=2)

    return output_dir


def prepare_data(cfg, accelerator, output_dir) -> Tuple[DataLoader, DataLoader]:
    """prepare training data"""
    logger.info(f"Creating VLA Dataset with Mixture `{cfg.datasets.vla_data.data_mix}`")
    vla_train_dataloader = build_dataloader(cfg=cfg, dataset_py=cfg.datasets.vla_data.dataset_py)

    vlm_train_dataloader = build_dataloader(cfg=cfg, dataset_py=cfg.datasets.vlm_data.dataset_py)

    accelerator.dataloader_config.dispatch_batches = False
    dist.barrier()

    return vla_train_dataloader, vlm_train_dataloader


def setup_optimizer_and_scheduler(model, cfg) -> Tuple[torch.optim.Optimizer, torch.optim.lr_scheduler._LRScheduler]:
    """set optimizer and learning rate scheduler"""
    # initialize optimizer
    param_groups = build_param_lr_groups(model=model, cfg=cfg)
    optimizer = torch.optim.AdamW(
        param_groups,
        lr=cfg.trainer.learning_rate.base,
        betas=tuple(cfg.trainer.optimizer.betas),
        weight_decay=cfg.trainer.optimizer.weight_decay,
        eps=cfg.trainer.optimizer.eps,
    )

    # print optimizer group information
    if dist.is_initialized() and dist.get_rank() == 0:
        for i, group in enumerate(optimizer.param_groups):
            logger.info(f"LR Group {group['name']}: lr={group['lr']}, num_params={len(group['params'])}")

    # initialize learning rate scheduler
    lr_scheduler = get_scheduler(
        name=cfg.trainer.lr_scheduler_type,
        optimizer=optimizer,
        num_warmup_steps=cfg.trainer.num_warmup_steps,
        num_training_steps=cfg.trainer.max_train_steps,
        scheduler_specific_kwargs=cfg.trainer.scheduler_specific_kwargs,  # minimum learning rate
    )

    return optimizer, lr_scheduler


class AsyncS3Sync:
    """
    保证：如果在运行中又请求同步，会记 pending；
    当前 sync 结束后会自动再跑一次，把新增文件补上。
    """
    def __init__(self, local_dir: str, s3_uri: str, log_path: str, poll_sec: float = 5.0):
        self.local_dir = local_dir
        self.s3_uri = s3_uri
        self.log_path = log_path
        self.poll_sec = poll_sec

        self.proc = None
        self.logf = None
        self.pending = False

        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._watcher = threading.Thread(target=self._watch_loop, daemon=True)
        self._watcher.start()

    def request_sync(self) -> bool:
        """
        训练线程调用这个。
        返回 True 表示“这次调用启动了一个新的 sync”；
        返回 False 表示“当时在跑，已记录 pending，会在结束后自动补跑”。
        """
        with self._lock:
            # 正在跑：不并发，改为 pending
            if self.proc is not None and self.proc.poll() is None:
                self.pending = True
                return False

            # 没在跑：直接启动
            self._start_locked()
            return True

    def _start_locked(self):
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)

        # 关旧 log fd，避免泄漏
        if self.logf is not None:
            try:
                self.logf.close()
            except Exception:
                pass
        self.logf = open(self.log_path, "a", buffering=1)

        cmd = [
            "aws", "s3", "sync",
            self.local_dir,
            self.s3_uri,
            "--only-show-errors",
        ]
        self.proc = subprocess.Popen(cmd, stdout=self.logf, stderr=self.logf)
        self.pending = False  # 启动新 sync 时清 pending

    def _watch_loop(self):
        while not self._stop.is_set():
            time.sleep(self.poll_sec)
            with self._lock:
                if self.proc is None:
                    continue
                # 还在跑
                if self.proc.poll() is None:
                    continue

                # 已结束：如果有人请求过 pending，就立刻补跑一次
                if self.pending:
                    self._start_locked()

    def close(self, wait: bool = True):
        """
        训练结束时调用：
        - wait=True：尽量把 pending 的同步也跑完
        """
        if wait:
            while True:
                with self._lock:
                    running = (self.proc is not None and self.proc.poll() is None)
                    pend = self.pending
                if not running and not pend:
                    break
                time.sleep(2.0)

        self._stop.set()
        with self._lock:
            if self.logf is not None:
                try:
                    self.logf.close()
                except Exception:
                    pass


class VLAMTrainer(TrainerUtils):
    def __init__(self, cfg, model, vla_train_dataloader, vlm_train_dataloader, optimizer, lr_scheduler, accelerator):
        self.config = cfg
        self.model = model
        self.vla_train_dataloader = vla_train_dataloader
        self.vlm_train_dataloader = vlm_train_dataloader
        self.optimizer = optimizer
        self.lr_scheduler = lr_scheduler
        self.accelerator = accelerator

        # training status tracking
        self.completed_steps = 0
        self.total_batch_size = self._calculate_total_batch_size()

    def prepare_training(self):
        rank = dist.get_rank() if dist.is_initialized() else 0
        seed = self.config.seed + rank if hasattr(self.config, "seed") else rank + 3047
        set_seed(seed)

        # load pretrained weights
        if hasattr(self.config.trainer, "pretrained_checkpoint") and self.config.trainer.pretrained_checkpoint:
            pretrained_checkpoint = self.config.trainer.pretrained_checkpoint
            reload_modules = (
                self.config.trainer.reload_modules if hasattr(self.config.trainer, "reload_modules") else None
            )
            self.model = self.load_pretrained_backbones(self.model, pretrained_checkpoint, reload_modules=reload_modules)

        # freeze parameters
        freeze_modules = (
            self.config.trainer.freeze_modules
            if (self.config and hasattr(self.config.trainer, "freeze_modules"))
            else None
        )
        self.model = self.freeze_backbones(self.model, freeze_modules=freeze_modules)

        #  print trainable parameters of the model
        self.print_trainable_parameters(self.model)

        # initialize distributed training components
        self.model, self.optimizer, self.vla_train_dataloader, self.vlm_train_dataloader = (
            self.setup_distributed_training(
                self.accelerator, self.model, self.optimizer, self.vla_train_dataloader, self.vlm_train_dataloader
            )
        )

        self._init_wandb()
        self._init_checkpointing()

    def _calculate_total_batch_size(self):
        """calculate global batch size"""
        return (
            self.config.datasets.vla_data.per_device_batch_size
            * self.accelerator.num_processes
            * self.accelerator.gradient_accumulation_steps
        )

    def _init_wandb(self):
        """initialize Weights & Biases"""
        if self.accelerator.is_main_process:
            wandb.init(
                name=self.config.run_id,
                dir=os.path.join(self.config.output_dir, "wandb"),
                project=self.config.wandb_project,
                entity=self.config.wandb_entity,
                group="vla-train",
            )

    def _init_checkpointing(self):
        """initialize checkpoint directory"""
        self.checkpoint_dir = os.path.join(self.config.output_dir, "checkpoints")
        os.makedirs(self.checkpoint_dir, exist_ok=True)
        
        # 初始化 S3 sync（只在主进程）
        if self.accelerator.is_main_process:
            run_id = self.config.run_id  # internvla_h10w_joint_real_vr_l500_r500
            bucket = getattr(self.config, "s3_bucket", None)
            if bucket:  # 有配置才启用
                s3_uri = f"s3://{bucket}/Checkpoints/{run_id}/"
                self.s3sync = AsyncS3Sync(
                    self.config.output_dir,
                    s3_uri,
                    log_path=os.path.join(self.config.output_dir, "s3_sync.log"),
                )
            else:
                self.s3sync = None
                if self.accelerator.is_main_process:
                    self.accelerator.print("🟨 s3_bucket 未配置，跳过 S3 sync 初始化")
        else:
            self.s3sync = None
            
        pretrained_checkpoint = getattr(self.config.trainer, "pretrained_checkpoint", None)
        is_resume = getattr(self.config.trainer, "is_resume", False)

        # resume training state
        if pretrained_checkpoint and is_resume:
            self._load_checkpoint(self.config.resume_from_checkpoint)

    def _load_checkpoint(self, checkpoint_path):
        """load checkpoint"""
        self.accelerator.load_state(checkpoint_path)
        self.accelerator.print(f"Resumed from checkpoint: {checkpoint_path}")

    def _save_checkpoint(self):
        """save current training state"""

        if self.accelerator.is_main_process:

            checkpoint_path = os.path.join(self.checkpoint_dir, f"steps_{self.completed_steps}")
            # save model state
            state_dict = self.accelerator.get_state_dict(self.model)
            torch.save(state_dict, checkpoint_path + "_pytorch_model.pt")

            # save training metadata
            summary_data = {
                "steps": self.completed_steps,
            }
            with open(os.path.join(self.config.output_dir, "summary.jsonl"), "a") as f:
                f.write(json.dumps(summary_data) + "\n")
            self.accelerator.print(f"✅ Checkpoint saved at {checkpoint_path}")
            
            if self.accelerator.is_main_process and self.s3sync:
                started = self.s3sync.request_sync()
                if started:
                    self.accelerator.print("🟦 Started background S3 sync")
                else:
                    self.accelerator.print("🟨 S3 sync running; marked pending (will sync again after finish)")

            # ✅ Save accessed configuration only
            if isinstance(self.config, AccessTrackedConfig):
                logger.info("📊 Saving accessed configuration...")
                output_dir = Path(self.config.output_dir)
                # self.config.save_accessed_config(
                #     output_dir / "config.json", 
                #     use_original_values=False
                # )
                self.config.save_accessed_config(
                    output_dir / "config.yaml", 
                    use_original_values=False 
                )
                logger.info("✅ Configuration files saved")

        self.accelerator.wait_for_everyone()

    def _log_metrics(self, metrics):
        """record training metrics"""
        if (
            self.completed_steps % self.config.trainer.logging_frequency == 0
        ):  # some parameters should be initialized for the class
            if dist.get_rank() == 0:

                # add learning rate
                metrics["learning_rate"] = self.lr_scheduler.get_last_lr()[0]

                # add epoch information
                metrics["epoch"] = round(self.completed_steps / len(self.vla_train_dataloader), 2)

                # record to W&B
                wandb.log(metrics, step=self.completed_steps)
                # debug output
                logger.info(f"Step {self.completed_steps}, Loss: {metrics})")

    def _create_data_iterators(self):
        """create data iterators"""
        self.vla_iter = iter(self.vla_train_dataloader)
        self.vlm_iter = iter(self.vlm_train_dataloader)

    def _get_next_batch(self):
        """get next batch (automatically handle data loop)"""
        try:
            batch_vla = next(self.vla_iter)
        except StopIteration:
            # check if there is self.vla_epoch_count
            if not hasattr(self, "vla_epoch_count"):
                self.vla_epoch_count = 0
            self.vla_iter, self.vla_epoch_count = TrainerUtils._reset_dataloader(
                self.vla_train_dataloader, self.vla_epoch_count
            )
            batch_vla = next(self.vla_iter)

        try:
            batch_vlm = next(self.vlm_iter)
        except StopIteration:
            if not hasattr(self, "vlm_epoch_count"):
                self.vlm_epoch_count = 0
            self.vlm_iter, self.vlm_epoch_count = self._reset_dataloader(self.vlm_train_dataloader, self.vlm_epoch_count)
            batch_vlm = next(self.vlm_iter)

        return batch_vla, batch_vlm

    def train(self):
        """execute training loop"""
        # print training config
        self._log_training_config()

        # prepare data iterators
        self._create_data_iterators()

        # create progress bar
        progress_bar = tqdm(
            range(self.config.trainer.max_train_steps), disable=not self.accelerator.is_local_main_process
        )
        
        try:
        # main training loop
            while self.completed_steps < self.config.trainer.max_train_steps:
                # get data batch
                t_start_data = time.perf_counter()
                batch_vla, batch_vlm = self._get_next_batch()
                t_end_data = time.perf_counter()
                # execute training step
                t_start_model = time.perf_counter()
                step_metrics = self._train_step(batch_vla, batch_vlm)
                t_end_model = time.perf_counter()
                # update progress
                if self.accelerator.sync_gradients:
                    progress_bar.update(1)
                    self.completed_steps += 1
                
                if self.accelerator.is_local_main_process:
                    progress_bar.set_postfix(
                            {
                                "data_times": f"{t_end_data - t_start_data:.3f}",
                                "model_times": f"{t_end_model - t_start_model:.3f}",
                            }
                        )

                # evaluate model
                if self.completed_steps % self.config.trainer.eval_interval == 0:
                    step_metrics = self.eval_action_model(step_metrics)

                # record metrics
                step_metrics["data_time"] = t_end_data - t_start_data
                step_metrics["model_time"] = t_end_model - t_start_model
                self._log_metrics(step_metrics)

                # save checkpoint
                if self.completed_steps % self.config.trainer.save_interval == 0 and self.completed_steps > 0:
                    self._save_checkpoint()

                    dist.barrier()  # ensure all processes are synchronized, avoid timeout

                # check termination condition
                if self.completed_steps >= self.config.trainer.max_train_steps:
                    break
            
        finally:
            # 不管正常结束还是异常，都尽量刷完同步
            if self.accelerator.is_main_process and getattr(self, "s3sync", None) is not None:
                self.accelerator.print("🟦 Exiting: waiting for pending S3 sync to complete...")
                self.s3sync.close(wait=True)

        # training end processing
        self._finalize_training()

        # execute evaluation step

    def eval_action_model(self, step_metrics: dict = None) -> float:
        """
        Evaluate the model on the given dataset using the specified metric function.

        :param eval_dataset: List of evaluation samples, each containing 'image', 'instruction', and 'action'.
        :param metric_fn: Function to compute the distance between predicted and ground truth actions.
        :return: Average metric score across the evaluation dataset.
        """

        if self.accelerator.is_main_process:

            examples, vlm_data = self._get_next_batch()

            score = 0.0
            num_samples = len(examples)
            actions = [example["action"] for example in examples]  # label

            # Predict actions using the model
            output_dict = self.model.predict_action(
                examples=examples
            )

            normalized_actions = output_dict["normalized_actions"]  # B, T, D

            actions = np.array(actions)  # convert actions to numpy.ndarray
            # B, Chunk, dim = actions.shape
            num_pots = np.prod(actions.shape)
            # Compute the metric score
            score = TrainerUtils.euclidean_distance(normalized_actions, actions)
            average_score = score / num_pots
            step_metrics["mse_score"] = average_score

        dist.barrier()
        return step_metrics

    def _log_training_config(self):
        """record training config"""
        if self.accelerator.is_main_process:
            logger.info("***** Training Configuration *****")
            logger.info(f"  Total optimization steps = {self.config.trainer.max_train_steps}")
            logger.info(f"  Per device batch size = {self.config.datasets.vla_data.per_device_batch_size}")
            logger.info(f"  Gradient accumulation steps = {self.config.trainer.gradient_accumulation_steps}")
            logger.info(f"  Total batch size = {self.total_batch_size}")

    def _train_step(self, batch_vla, batch_vlm):
        """execute single training step"""
        log_dict = {}
        with self.accelerator.accumulate(self.model):
            self.optimizer.zero_grad()

            # VLA task forward propagation
            with torch.autocast("cuda", dtype=torch.bfloat16):
                output_dict = self.model.forward(batch_vla)
                action_loss = output_dict["action_loss"]
                total_loss = action_loss
            self.accelerator.backward(total_loss)

            
            pass
            # VLM task forward propagation
            with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                vlm_output = self.model.qwen_vl_interface(**batch_vlm)
                vlm_loss = vlm_output.loss * self.config.trainer.loss_scale.vlm

            self.accelerator.backward(vlm_loss)

            pass

            
            # gradient clipping
            if self.config.trainer.gradient_clipping is not None:
                self.accelerator.clip_grad_norm_(self.model.parameters(), self.config.trainer.gradient_clipping)

            # optimizer step
            self.optimizer.step()
            self.lr_scheduler.step()

            log_dict.update(
                {
                    "action_dit_loss": action_loss.item(),
                    "vlm_loss": vlm_loss.item(),
                }
            )
        return log_dict

    def _finalize_training(self):
        """training end processing"""
        # save final model
        if self.accelerator.is_main_process:
            final_checkpoint = os.path.join(self.config.output_dir, "final_model")
            os.makedirs(final_checkpoint, exist_ok=True)
            state_dict = self.accelerator.get_state_dict(self.model)
            torch.save(state_dict, os.path.join(final_checkpoint, "pytorch_model.pt"))
            logger.info(f"Training complete. Final model saved at {final_checkpoint}")

        # close W&B
        if self.accelerator.is_main_process:
            wandb.finish()

        self.accelerator.wait_for_everyone()


def main(cfg) -> None:
    logger.info("VLA Training :: Warming Up")

    #  Wrap config to enable access tracking
    cfg = wrap_config(cfg)
    logger.info("✅ Configuration wrapped for access tracking")

    # create output directory and save config
    output_dir = setup_directories(cfg=cfg)

    # build model
    vla = build_framework(cfg)
    # prepare data
    vla_train_dataloader, vlm_train_dataloader = prepare_data(cfg=cfg, accelerator=accelerator, output_dir=output_dir)
    # set optimizer and scheduler
    optimizer, lr_scheduler = setup_optimizer_and_scheduler(model=vla, cfg=cfg)

    # create trainer
    # Run VLA Training
    trainer = VLAMTrainer(
        cfg=cfg,
        model=vla,
        vla_train_dataloader=vla_train_dataloader,
        vlm_train_dataloader=vlm_train_dataloader,
        optimizer=optimizer,
        lr_scheduler=lr_scheduler,
        accelerator=accelerator,
    )

    # execute training preparation
    trainer.prepare_training()
    # execute training
    trainer.train()

    # And... we're done!
    logger.info("... and that's all, folks!")
    dist.barrier()
    dist.destroy_process_group()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_yaml", type=str, default="starVLA/config/training/starvla_cotrain_oxe.yaml", help="Path to YAML config")
    args, clipargs = parser.parse_known_args()

    # Load YAML config & Convert CLI overrides to dotlist config
    cfg = OmegaConf.load(args.config_yaml)
    dotlist = normalize_dotlist_args(clipargs)  # Normalize CLI args to dotlist format
    cli_cfg = OmegaConf.from_dotlist(dotlist)
    cfg = OmegaConf.merge(cfg, cli_cfg)

    # if cfg.is_debug:
    if cfg.is_debug and dist.is_initialized() and dist.get_rank() == 0:
        import debugpy

        debugpy.listen(("0.0.0.0", 10092))
        print(
            "🔍 Rank 0 waiting for debugger attach on port 10092..."
        )  # you may ask chatGPT what is debugger attach in vscode
        debugpy.wait_for_client()

    main(cfg)
