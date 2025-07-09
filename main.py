"""
main.py - Player Re-Identification Script

This script uses a YOLO model from Ultralytics for player detection and Deep SORT for tracking.

NOTE:
- By default, this script loads the model defined by MODEL_NAME.
- You can replace MODEL_NAME with the provided 'yolov11.pt' weights file.
- If you don't have 'yolov11.pt', you can test with 'yolov8n.pt' (Ultralytics official release).
"""


# main.py

from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2
import random
import os

# CONFIGURATION
INPUT_VIDEO = "15sec_input_720p.mp4"
OUTPUT_VIDEO = "tracked_output.mp4"
MODEL_NAME = "yolov8n.pt"  # Replace with yolov11.pt if available

# INITIALIZE YOLO MODEL
print("Loading YOLO model...")
model = YOLO(MODEL_NAME)

# INITIALIZE DEEP SORT TRACKER
tracker = DeepSort(max_age=30)
id_colors = {}

# VIDEO SETUP
cap = cv2.VideoCapture(INPUT_VIDEO)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

print("Processing video...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO Detection
    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label != 'person':
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        w, h = x2 - x1, y2 - y1
        conf = float(box.conf[0])
        detections.append(([x1, y1, w, h], conf, label))

    # Deep SORT Tracking
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())

        # Assign random color for each player ID
        if track_id not in id_colors:
            id_colors[track_id] = [random.randint(0, 255) for _ in range(3)]
        color = id_colors[track_id]

        # Draw bounding box and ID
        cv2.rectangle(frame, (l, t), (r, b), color, 2)
        cv2.putText(frame, f'Player {track_id}', (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    out.write(frame)

# Release everything
cap.release()
out.release()
print(f"Output saved to: {OUTPUT_VIDEO}")
