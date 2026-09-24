import cv2
import mediapipe as mp
import os
import urllib.request
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#Just downloading the model file
model_path = "hand_landmarker.task"
if not os.path.exists(model_path):
    print("Downloading hand tracking model (~9 MB)... please wait a moment.")
    url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
    urllib.request.urlretrieve(url, model_path)
    print("Model ready!")

base_options = python.BaseOptions(
    model_asset_path=model_path
) #basically creating options that say "use this model"

#creating options
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),           # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),           # Index finger
    (5, 9), (9, 10), (10, 11), (11, 12),      # Middle finger
    (9, 13), (13, 14), (14, 15), (15, 16),    # Ring finger
    (13, 17), (17, 18), (18, 19), (19, 20),   # Pinky
    (0, 17)                                   # Palm base
]

cap = cv2.VideoCapture(0)



while True:
    #frame is the image, represented as a numpy array
    success, frame = cap.read()
    if success == False:
        print("camera is not available")
        break

    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    detection_result = detector.detect(mp_image)

    if detection_result.hand_landmarks:
        # detection_result.hand_landmarks is a list of detected hands
        for hand in detection_result.hand_landmarks:
            pixel_points = []
            for lm in hand: #lm = landmark
                px = int(lm.x * w)
                py = int(lm.y * h)
                pixel_points.append((px, py))

            # 2. Draw the connection lines (bones)
            for start_idx, end_idx in HAND_CONNECTIONS:
                pt1 = pixel_points[start_idx]
                pt2 = pixel_points[end_idx]
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            for idx, (px, py) in enumerate(pixel_points):
                # Make fingertips (4, 8, 12, 16, 20) blue, other joints red
                if idx in [4, 8, 12, 16, 20]:
                    cv2.circle(frame, (px, py), 8, (255, 0, 0), -1)  # Blue fingertip
                else:
                    cv2.circle(frame, (px, py), 5, (0, 0, 255), -1)  # Red joint
            
    else:
        print("No hand in frame")

    cv2.imshow("webcam", frame) # Display the frame in a window

    #(cv2.waitKey(1) & 0xFF) just takes the last 8 bits of a key "q"
    if (cv2.waitKey(1) & 0xFF) == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()