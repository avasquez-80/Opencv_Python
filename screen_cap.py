import numpy as np
import cv2
from PIL import ImageGrab #ImageGrab solo funciona en Windows y MacOS

def capture_screen(bbox=(50,50,690,530)):
    cap_scr = np.array(ImageGrab.grab(bbox))
    cap_scr = cv2.cvtColor(cap_scr,cv2.COLOR_RGB2BGR)
    return cap_scr

while True:
    timer = cv2.getTickCount()
    img = capture_screen()
    fps = cv2.getTickFrequency() / (cv2.getTickCount()-timer)
    cv2.putText(img,'FPS{}'.format(int(fps)),(75,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(20,230,20),2)
    cv2.imshow('Screen Capture',img)
    cv2.waitKey(1)