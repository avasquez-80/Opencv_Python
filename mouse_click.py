import cv2
import numpy as np

circles = np.zeros((4,2),np.int0)
contador = 0

def mouse_points(event,x,y,flags,params):
    global contador
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[contador] = x,y
        contador += 1
        print(circles)
 
img = cv2.imread('./archivos/cards.jpg')

while True:
    if contador == 4:
        width,height = 250,350
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        archivo_salida = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow('Archivo de salida',archivo_salida)

    for x in range(4):
        cv2.circle(img,(int(circles[x][0]),int(circles[x][1])),5,(255,0,0),cv2.FILLED)

    if cv2.waitKey(1) == ord('x'):
        break
    
    cv2.imshow('Cartas',img)
    cv2.setMouseCallback("Cartas",mouse_points) # debe tener el mismo nombre de ventana que el que se muestra en la imagen ('Cartas')
    cv2.waitKey(1) # con waitKey(1) funciono correctamente
