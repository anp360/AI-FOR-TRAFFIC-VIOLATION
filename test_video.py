import cv2

video_path = 'traffic.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Could not open video file:", video_path)
else:
    print("✅ Successfully opened video.")
    print("FPS:", cap.get(cv2.CAP_PROP_FPS))
    print("Resolution:", int(cap.get(3)), "x", int(cap.get(4)))

cap.release()

