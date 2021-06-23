import cv2
import numpy as np

kernel = np.ones((4,4),np.uint8)
cap = cv2.VideoCapture(0)

while True:
    res, frame = cap.read()
    #img = cv2.imshow('Video',frame)
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(7,7),2)
    img = cv2.Canny(img,100,200)
    img = cv2.dilate(img,kernel,iterations=3)
    img = cv2.erode(img,kernel,iterations=1)

    cv2.imshow('ventanita',img)

    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows