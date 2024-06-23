import cv2
import os
import pickle
import face_recognition
import numpy as np

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
skip_frames = 5
frame_count = 0

# Load the Encoding File
print("Loading encodings...")
encodings = open("Encodings.p", "rb")
encodingListKnownWithIDs = pickle.load(encodings)
encodings.close()
encodeListKnown, studentIDs = encodingListKnownWithIDs
print("Encodings loaded.")

while True:
    success, img = cap.read()

    frame_count += 1
    if frame_count % skip_frames == 0:

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)    

        faceCurrentFrame = face_recognition.face_locations(imgS)
        encodeCurrentFrame = face_recognition.face_encodings(imgS,faceCurrentFrame)

        imgBackground[120:120 + 480, 68:68 + 640] = img
        imgBackground[30:30 + 180, 780:780 + 450] = imgModeList[0]
        cv2.imshow("Face Attendance", imgBackground)

        for encodeFace, faceLocation in zip(encodeCurrentFrame, faceCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDistance)
            

    # Wait for a key press to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
