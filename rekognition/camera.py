import cv2
import time

starttime = time.time()

import time

def take_photo():
    current_time = time.ctime()
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('webcamphoto' + str(current_time) + '.jpg', frame)
    cap.release()
    print("photo taken")

def main():
    take_photo()
    

while (True): 
    main()
    time.sleep(15 - ((time.time() - starttime) % 15))