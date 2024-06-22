import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

imgBackground = cv2.imread("Resources/Attendance.png")

### Importing the modes
modePath = os.listdir("Resources/Modes")
imgModeList = []
for path in modePath:
    imgModeList.append(cv2.imread(f"Resources/Modes/{path}"))

# Number of frames to skip
skip_frames = 2
frame_count = 0

while True:
    success, img = cap.read()
    frame_count += 1
    if frame_count % skip_frames == 0:
        imgBackground[120:120 + 480, 68:68 + 640] = img
        imgBackground[30:30 + 180, 780:780 + 450] = imgModeList[0]
        cv2.imshow("Face Attendance", imgBackground)

    # Wait for a key press to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
