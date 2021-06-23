import cv2
import numpy as np
import random

def ram_color():
    color = []
    for colorcito in range (3):
        color.append(random.randint(0,255))
    return(color)

img = np.zeros((600,600,3),np.uint8)
color = [255,0,0]

cv2.line(img,(0,0),(img.shape[0],img.shape[1]),ram_color(),3)
cv2.rectangle(img,(50,100),(150,300), ram_color(),2)
cv2.circle(img,(400,500),20,ram_color(),-1)
cv2.putText(img,'Practicando Python',(20,70),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,ram_color(),2)

cv2.imshow('DIbujo',img)
cv2.waitKey(0)