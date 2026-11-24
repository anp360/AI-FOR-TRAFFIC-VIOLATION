# calibrate_px_to_m.py
# Cross-platform version (no cv2.imshow needed)
import cv2, sys, math
import matplotlib.pyplot as plt

VIDEO = 'traffic.mp4'

# --- Grab first frame from video ---
cap = cv2.VideoCapture(VIDEO)
if not cap.isOpened():
    print("❌ Cannot open", VIDEO)
    sys.exit(1)

ret, frame = cap.read()
cap.release()
if not ret:
    print("❌ Can't read frame from", VIDEO)
    sys.exit(1)

# --- Show frame with matplotlib and let user click ---
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.title("Click TWO points with known real-world distance,\nthen close window")
pts = plt.ginput(2)  # exactly two clicks
plt.close()

if len(pts) < 2:
    print("❌ Not enough points clicked")
    sys.exit(1)

# --- Calculate pixel distance ---
p1, p2 = pts[0], pts[1]
pixel_dist = math.hypot(p1[0]-p2[0], p1[1]-p2[1])
print("📏 Pixel distance:", pixel_dist)

# --- Ask for real distance in meters ---
real_m = float(input("Enter the real-world distance between these points in METERS: "))
px_to_m = real_m / pixel_dist

print("\n✅ Calibration complete!")
print(f"👉 1 pixel ≈ {px_to_m:.6f} meters")

