---
name: computer-vision-experiential
description: >-
  Experiential Computer Vision using OpenCV, MediaPipe real-time hand/pose tracking,
  and lightweight YOLO object detection. Connects visual aesthetics and athletic movement
  to real-time spatial neural networks on laptop webcams.
---

# Experiential Computer Vision: Real-Time Spatial AI

This skill enables visual experimentation with computer vision and live camera pipelines.

## 1. 15-Line Live Webcam Hand & Motion Tracker (MediaPipe)
Run this script to track hand keypoints and wrist angles in real time:
```python
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break
    
    # Flip for natural selfie-view
    image = cv2.flip(image, 1)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    cv2.imshow('Sentinel Real-Time Spatial Vision', image)
    if cv2.waitKey(5) & 0xFF == 27: # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
```

## 2. YOLO Object Detection in 5 Lines
Detect everyday objects, sports gear, and humans with pre-trained weights:
```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt') # Lightweight nano model
results = model.predict(source=0, show=True) # Runs live on webcam
```

## 3. Connecting Vision to Athletic Performance
* Track hand speed across frames to calculate reaction impulse.
* Detect table tennis balls and draw parabolic flight trajectories across consecutive camera frames.
