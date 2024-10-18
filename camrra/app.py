import streamlit as st
import cv2

st.title("Video Stream")

# 打开视频文件或摄像头
video_source = 0  # 0 表示默认摄像头
cap = cv2.VideoCapture(video_source)

# 创建一个占位符
frame_placeholder = st.empty()

# 读取视频流并显示
while True:
    ret, frame = cap.read()
    if not ret:
        st.write("无法读取视频流")
        break
    frame_placeholder.image(frame, channels="BGR")