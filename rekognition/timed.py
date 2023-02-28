import time
import cv2 

vid = cv2.VideoCapture(0)

starttime = time.time()

ret, frame = vid.read()
cv2.imshow('Test', frame)

while(True):
    
    print("tick")

    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


