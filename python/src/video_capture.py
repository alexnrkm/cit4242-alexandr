import cv2

cap = cv2.VideoCapture(0)

while True:
    #frame is the image, represented as a numpy array
    success, frame = cap.read()
    if success == False:
        print("camera is not available")
        break

    cv2.imshow("webcam", frame) # Display the frame in a window

    #(cv2.waitKey(1) & 0xFF) just takes the last 8 bits of a key "q"
    if (cv2.waitKey(1) & 0xFF) == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()