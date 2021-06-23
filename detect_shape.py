import cv2
import numpy as np
from funciones import stack_images

frame_width, frame_height = 640,480
cap = cv2.VideoCapture(2)
cap.set(3,frame_width)
cap.set(4,frame_height)

def empty(a):
    pass

cv2.namedWindow('Parametros')
cv2.resizeWindow('Parametros',640,240)
cv2.createTrackbar('thd1','Parametros',0,255,empty)
cv2.createTrackbar('thd2','Parametros',0,255,empty)
cv2.createTrackbar('area','Parametros',0,30000,empty)


def det_contours(img, img_contour):
    contour, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        area_min = cv2.getTrackbarPos('area','Parametros') #trackbar necesario para area
        if area > area_min:
            cv2.drawContours(img_contour,cnt,-1,(255,0,255),7)
            peri = cv2.arcLength(cnt,True)
            aprox = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(aprox))
            x,y,w,h = cv2.boundingRect(aprox)
            cv2.rectangle(img_contour,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(img_contour,'Points'+str(len(aprox)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,.7,(0,255,0),2)
            cv2.putText(img_contour,'Area'+str(int(area)),(x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,.7,(0,255,0),2)

while True:
    _,img = cap.read()
    img_contour = img.copy()
    img_blur = cv2.GaussianBlur(img,(7,7),1)
    img_gray = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)
    thd1,thd2 = cv2.getTrackbarPos('thd1','Parametros'),cv2.getTrackbarPos('thd2','Parametros')
    img_canny = cv2.Canny(img_gray,thd1,thd2)
    kernel = np.ones((5,5))
    img_dil = cv2.dilate(img_canny,kernel,iterations=1)
    det_contours(img_dil,img_contour)

    img_stack = stack_images.stack_images(0.8,([img,img_blur,img_gray],
                                                    [img_canny,img_dil,img_contour]))
    cv2.imshow('Video',img_stack)
    if cv2.waitKey(1) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows