import cv2
import time

cap = cv2.VideoCapture('/dev/video5')

# allow the camera to warmup

time.sleep(0, 1)
ret, frame = cap.read()
print(ret, frame)