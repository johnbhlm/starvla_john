

cd /mnt/petrelfs/yejinhui/Projects/starVLA
export PYTHONPATH=$(pwd):${PYTHONPATH}

port=6678
gpu_id=2
# export DEBUG=true
export star_vla_python=/mnt/petrelfs/share/yejinhui/Envs/miniconda3/envs/starVLA/bin/python

your_ckpt=./results/Checkpoints/1208_bridge_rt_1_QwenPI_qwen2.5/checkpoints/steps_80000_pytorch_model.pt

#### run server #####
CUDA_VISIBLE_DEVICES=${gpu_id} ${star_vla_python} deployment/model_server/server_policy.py \
    --ckpt_path ${your_ckpt} \
    --port ${port} \
    --use_bf16 \
    2>&1 | tee "${log_file}"