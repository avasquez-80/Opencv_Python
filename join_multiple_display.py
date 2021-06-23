import numpy as np
import cv2
from funciones import func_mult_disp

frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)

while True:
    success, img = cap.read()
    kernel = np.ones((5,5),np.uint8)
    print(kernel)

    #path = './archivos/futbol.jpg'
    #img = cv2.imread(path)
    img = cv2.resize(img,(0,0),fx=0.8,fy=0.8)
    imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imGray,(7,7),0)
    imgCanny = cv2.Canny(imgBlur,100,200)
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)
    imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

    stacked_images = func_mult_disp.stack_images(([img,imGray,imgBlur],
                                            [imgCanny,imgDilation,imgEroded]),0.6)
    cv2.imshow('Stacked Images',stacked_images)
    if cv2.waitKey(1) == ord('x'):
        break
    # cv2.imshow('lena',img)
    # cv2.imshow('GrayScale',imGray)
    # cv2.imshow('Img Blur',imgBlur)
    # cv2.imshow('Img Canny',imgCanny)
    # cv2.imshow('Img Dilation', imgDilation)
    # cv2.imshow('Img Erosion', imgEroded)

    # cv2.waitKey(0)
    #cv2.destroyAllWindows