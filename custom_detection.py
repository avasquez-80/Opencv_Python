import cv2

######################################################
path = '/home/alejandro/Proyectos/ProyectosNuevos/Python/practicas/opencv/practicas/haar_cascade/data/haarcascade_smile.xml' #path of the cascade
camera_no = 0           #Camera number
object_name = 'face'    #Object name to display
frame_width = 640       #Display width
frame_height = 480      #Display height
color = (255,0,255)
######################################################

cap = cv2.VideoCapture(camera_no)
cap.set(3,frame_width)
cap.set(4,frame_height)

def empty(a):
    pass

#Create taskbar
cv2.namedWindow('Result')
cv2.resizeWindow('Result',frame_width,frame_height-100)
cv2.createTrackbar('Scale','Result',400,1000,empty)
cv2.createTrackbar('Neig','Result',8,50,empty)
cv2.createTrackbar('Min Area','Result',0,100000,empty)
cv2.createTrackbar('Brightness','Result',180,255,empty)

#Load de clasifiers downloaded
#cascade = cv2.CascadeClassifier('/home/alejandro/Proyectos/ProyectosNuevos/Python/practicas/opencv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier(path)
while True:
    #Set Camera value from trackbar brightness
    camera_brightness = cv2.getTrackbarPos('Brightness','Result')
    cap.set(10,camera_brightness)
    #Get camera image and convert to gray
    succes, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Detect object using the cascade
    scale_val1=1+(cv2.getTrackbarPos('Scale','Result')/1000)
    neig=cv2.getTrackbarPos('Neig','Result')
    objects = cascade.detectMultiScale(gray,scale_val1,neig)
    #Display the detected object
    for (x,y,w,h) in objects:
        area = w*h
        min_area = cv2.getTrackbarPos('Min Area','Result')
        if area > min_area:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,object_name,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h,x:x+w]
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows