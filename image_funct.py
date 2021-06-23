import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = './archivos/futbol.jpg'
img = cv2.imread(path)
img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

cv2.imshow('lena',img)
cv2.imshow('GrayScale',imGray)
cv2.imshow('Img Blur',imgBlur)
cv2.imshow('Img Canny',imgCanny)
cv2.imshow('Img Dilation', imgDilation)
cv2.imshow('Img Erosion', imgEroded)

cv2.waitKey(0)
#cv2.destroyAllWindows