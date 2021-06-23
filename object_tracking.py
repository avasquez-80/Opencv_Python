import cv2

tracker = cv2.TrackerMOSSE_create()

cap = cv2.VideoCapture(0)
succes,frame = cap.read()
bbox = cv2.selectROI('Video',frame,False)
tracker.init(frame, bbox)

while True:
    timer = cv2.getTickCount()
    succes,img = cap.read()
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    
    cv2.putText(img,str(int(fps)),(75,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.imshow('Video',img)

    if cv2.waitKey(1) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows