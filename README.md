# Player Re-Identification in a Single Video Feed
Player re identification in a single video feed using YOLOv11 and Deep SORT
This project performs player tracking and re-identification in a 15-second football video clip. The goal is to ensure that each player retains the same identity (ID), even after going out of frame and returning later.
# Project structure
player-reid-single-feed/
├── src/
│ └── main.py # Detection + tracking code
├── 15sec_input_720p.mp4 # Input video (place in root directory)
├── tracked_output.mp4 # Output video with player IDs
├── requirements.txt # Python dependencies
|__ README.md # This file
# Setup instructions

1. Clone the repository:
git clone https://github.com/Rakonda-SANJANA/player_reidentification.git
cd player_reidentification
2. Install dependencies:
pip install -r requirements.txt
3. Place the input video 15sec_input_720p.mp4 in the root directory.
4. Run the tracking script:python src/main.py
5. The output video will be saved as tracked_output.mp4 in the root directory.
6. The detection code loads the model defined by the variable `MODEL_NAME` in `main.py`.If you have the yolov11.pt, place it in the project directory and set:  MODEL_NAME = "yolov11.pt"
7. If you do not have yolov11.pt, the pipeline can still run using the publicly available Ultralytics YOLOv8 nano model:MODEL_NAME = "yolov8n.pt"

