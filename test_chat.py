from starVLA.model.framework.M1 import InternVLA_M1
from starVLA.model.framework.QwenDual import Qwen_Dual
from PIL import Image
import requests
from io import BytesIO
import torch
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt

cap_top = cv2.VideoCapture("playground/Datasets/H10W_real_data_1128/lerobot_dataset_167/videos/chunk-000/observation.images.camera_high/episode_000001_h264.mp4")
video_left  = cv2.VideoCapture("playground/Datasets/H10W_real_data_1128/lerobot_dataset_167/videos/chunk-000/observation.images.camera_left_wrist/episode_000001_h264.mp4")
video_right = cv2.VideoCapture("playground/Datasets/H10W_real_data_1128/lerobot_dataset_167/videos/chunk-000/observation.images.camera_right_wrist/episode_000001_h264.mp4")  

# 获取输出视频参数
fps = cap_top.get(cv2.CAP_PROP_FPS)
width = int(cap_top.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap_top.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ===== 创建输出视频对象 =====
output_path = "star_output_with_result_head_lion.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

saved_model_path = "playground/Checkpoints/InternVLA-M1-Pretrain-RT-1-Bridge/checkpoints/steps_50000_pytorch_model.pt"
# saved_model_path = "/home/zhanrui.liao/vla_ws/InternVLA-M1/results/Checkpoints/InternVLA-M1-LIBERO-Object/checkpoints/steps_30000_pytorch_model.pt"
# saved_model_path = "playground/Checkpoints/1120_BEHAVIOR_challenge_QwenDual_taskall/checkpoints/steps_100000_pytorch_model.pt"
# saved_model_path = "playground/Checkpoints/1120_BEHAVIOR_challenge_QwenDual_taskall/checkpoints/steps_100000_pytorch_model.pt"
internVLA_M1 = InternVLA_M1.from_pretrained(saved_model_path)
# QwenDual = Qwen_Dual.from_pretrained(saved_model_path)

# Use the raw image link for direct download
instruction = "Give the bounding box of the orange lion toy"
# instruction = "Identigy several spots within the vacant space that's between the dinosaur doll and yellow duck"
# question = (
#             f"Task is: {instruction}. "
#             f"Based on the image, has the task been successfully completed? "
#             f"Answer only yes or no."
#         )
frame_id = 0

while True:
    ret, frame_bgr_top = cap_top.read()
    ret, frame_bgr_left = video_left.read()
    ret, frame_bgr_right = video_right.read()
    if not ret:
        break
    frame_id += 1
    # ===== 转换 BGR → RGB → PIL =====
    frame_rgb_top = cv2.cvtColor(frame_bgr_top, cv2.COLOR_BGR2RGB)
    img_top = Image.fromarray(frame_rgb_top, mode="RGB")
    frame_rgb_left = cv2.cvtColor(frame_bgr_left, cv2.COLOR_BGR2RGB)
    img_left = Image.fromarray(frame_rgb_left, mode="RGB")
    frame_rgb_right = cv2.cvtColor(frame_bgr_right, cv2.COLOR_BGR2RGB)
    img_right = Image.fromarray(frame_rgb_right, mode="RGB")
    # ===== 大语言模型问答 =====
    response = internVLA_M1.chat_with_M1(
        image=img_top,
        text=instruction,
        max_new_tokens=64
    )
    # response = QwenDual.chat_with_Qwen(
        # image=img_top,
        # text=instruction,
        # max_new_tokens=64
    # )
    print(f"[Frame {frame_id:04d}]  {response}")
    
    # # ===== 把结果写到帧图像上 =====
    # draw_frame = frame_bgr_top.copy()
    # cv2.putText(
    #     draw_frame,
    #     f"{response}",
    #     (20, 40),
    #     cv2.FONT_HERSHEY_SIMPLEX,
    #     1.0,
    #     (0, 255, 0),
    #     1,
    #     cv2.LINE_AA
    # )
    # 取出字符串本体
    raw = response[0]
    clean = raw.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean)  # dict

    bbox = data["bbox_2d"]
    # print("bounding box: ", bbox)
    img = frame_bgr_top

    x1, y1, x2, y2 = bbox
    if not isinstance(img, np.ndarray):
        img = np.array(img)
    # print("img shape:", img.shape)
    # 画框
    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
    # plt.imshow(frame_bgr_top)  # BGR → RGB
    # plt.show()
    # ===== 写入输出视频 =====
    writer.write(img)

cap_top.release()
video_left.release()
video_right.release()
writer.release()
print("Processing finished!")


# # instruction = "Give the bounding box for the yellow duck."
# print("instruction:", instruction)
# response = self.chat_with_M1(batch_images[0][0], instruction)
# # 取出字符串本体
# raw = response[0]
# # 去除 ```json 和 ```
# clean = raw.replace("```json", "").replace("```", "").strip()
# # 解析 JSON
# data = json.loads(clean)
# # 提取 bbox
# bboxes = [item["bbox_2d"] for item in data]
# print("bounding box of yellow duck: ", bboxes)
# img = batch_images[0][0]

# x1, y1, x2, y2 = bboxes[0]
# if not isinstance(img, np.ndarray):
#     img = np.array(img)
# print("img shape:", img.shape)
# # 画框
# cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)

# plt.imshow(img)  # BGR → RGB
# plt.show()
