# Player Re-Identification Report 

# Objective

To identify and consistently track players in a single 15-second football video. The goal was to assign consistent IDs to each player,even if they exited and re-entered the frame ,simulating real-time re-identification.
# Approach & Methodology

1. Detection:
   - Used the provided YOLOv11 model (fallback: YOLOv8n) for detecting 'person' class objects in each frame.
   - Loaded using the Ultralytics YOLO API.

2. Tracking:
   - Applied Deep SORT for real-time object tracking with re-identification.
   - Tracker used bounding box positions, detection confidence, and visual appearance features.

3. Player Identity Management:
   - Each player ID was assigned and maintained across frames.
   - If a player left the frame and reappeared, the tracker preserved the same ID (when possible).

4. Output:
   - Final video was generated with bounding boxes and unique player IDs consistently labeled throughout.


# Techniques Tried

- Tried different YOLO model sizes (e.g., yolov8n, yolov8s) for balance between speed and accuracy.
- Tuned `DeepSort` parameters like `max_age` to avoid losing track of temporarily disappeared players.
- Color-coded player IDs for better visual tracking in the output video.

# Challenges Faced

- YOLOv11 weights were not publicly available so fallback to YOLOv8n was used for testing.
- Some players overlapped frequently, making consistent ID assignment challenging.
- Short video length (15 sec) limited ability to evaluate long-term re-identification scenarios.

# Future Work

If more time and resources were available:
- Fine-tune YOLOv11 on more sports-specific datasets for improved accuracy.
- Integrate appearance-based embeddings (e.g., ReID features) to strengthen identity preservation.
- Simulate longer clips or multi-angle views to test real-world robustness.

# Conclusion

Despite constraints, the system successfully demonstrated real-time player detection and consistent ID tracking in a sports video. The modular code is clean, reproducible, and ready for further improvements.


Author: Sanjana  
Assignment: Sports Analytics - Player Re-Identification  
