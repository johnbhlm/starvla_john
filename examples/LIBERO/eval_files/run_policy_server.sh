#!/bin/bash

your_ckpt=./results/Checkpoints/1207_libero4in1_qwen3fast/checkpoints/steps_10000_pytorch_model.pt

base_port=10093
export star_vla_python=/mnt/petrelfs/share/yejinhui/Envs/miniconda3/envs/starVLA/bin/python
your_ckpt=results/Checkpoints/1208_libero_all_QwenPI_qwen3/checkpoints/steps_50000_pytorch_model.pt
gpu_id=7
port=5694
################# star Policy Server ######################

# export DEBUG=1

python deployment/model_server/server_policy.py \
    --ckpt_path ${your_ckpt} \
    --port ${port} \
    --use_bf16

# #################################
