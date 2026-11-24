import os
import cv2
from ultralytics import YOLO

# === Setup ===
video_path = 'traffic.mp4'
model_path = 'yolov8n.pt'  # This will auto-download if missing

# === Debug Info ===
print("Current directory:", os.getcwd())

print("Files:", os.listdir())

if not os.path.exists(video_path):
    raise FileNotFoundError(f"❌ '{video_path}' NOT FOUND!")
else:
    print(f"✅ Found '{video_path}'")

# === Load YOLOv8 model ===
print("📦 Loading YOLOv8 model...")
model = YOLO(model_path)
print("✅ Model loaded.")

# === Open video ===
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise RuntimeError("❌ Could not open video!")

# === Video Writer for output ===
width, height = int(cap.get(3)), int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

print("🚦 Starting detection... Press 'Q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("🔚 End of video.")
        break

    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].int().tolist()
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            # Filter to show only vehicles
            if label in ['car', 'truck', 'bus', 'motorbike', 'motorcycle']:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    out.write(frame)
    cv2.imshow('Traffic Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Quitting early...")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ Detection complete. Output saved to 'output.mp4'")
