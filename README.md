# AI for Traffic Violation Detection and Emergency Service Contact

A computer-vision prototype that uses YOLOv8 to detect vehicles in traffic video footage, as a foundation for automated traffic violation detection and emergency service alerting.

## Current functionality

- **`traffic_detection.py`** — Runs YOLOv8 (`yolov8n.pt`) on `traffic.mp4`, detects vehicles (car, truck, bus, motorbike), draws bounding boxes with confidence scores, and writes the annotated result to `output.mp4`.
- **`calibrate_px_to_m.py`** — Lets you click two points of known real-world distance on a video frame to compute a pixel-to-meter scale factor, needed for estimating vehicle speed from pixel motion.
- **`test_video.py`** — Quick sanity check that a video file opens correctly and reports its FPS/resolution.

## Project goal

Extend vehicle detection into full traffic violation detection (e.g. speeding, red-light running) and automatically notify emergency services when an incident is detected.

## Requirements

- Python 3
- `ultralytics` (YOLOv8)
- `opencv-python`
- `matplotlib`

## Usage

```bash
python traffic_detection.py
```
