import cv2
import numpy as np

# cap = cv2.VideoCapture('http://192.168.43.156:8080/video')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    frame = cv2.medianBlur(frame,9)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0,50,20], dtype=np.uint8)
    upper_skin = np.array([255,255,255], dtype=np.uint8)
    
    #extract skin colur imagw  
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break