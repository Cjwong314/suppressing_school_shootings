import cv2


webcam = cv2.VideoCapture(0)

def camera():
    check, frame = webcam.read()
    cv2.imshow('Test', frame)

def main():
    camera()


while True:
    main()
	