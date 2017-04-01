import cv2
import time

# reading frames one by one

# cv2.VideoCapture() - first parameter index of camera or file path to the movie file
video = cv2.VideoCapture(0)

a = 1

while True:
    a = a +1
    # check is boolean
    # frame is the first image captured by the camera
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # showing each frame of image captured
    cv2.imshow('capturing', gray)


    # releasing the camera after capturing
    key = cv2.waitKey(1)

    # video will stop when q will be pressed
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows