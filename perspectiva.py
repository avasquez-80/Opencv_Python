import cv2
import numpy as np

file = './archivos/cards.jpg'
archivo = cv2.imread(file)

width,height = 250,350
pts1=np.float32([[111,221],[290,188],[157,484],[355,443]])
#print(pts1)
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
#print(pts2)
matrix = cv2.getPerspectiveTransform(pts1,pts2)
archivo_salida = cv2.warpPerspective(archivo,matrix,(width,height))

#pt1 = (int(pts1[0][0]),pts1[0][1])
#print(pt1)

#pt2 = (pts1[1][0],pts1[1][1])
#print(pt2)

for x in range(4):
    cv2.circle(archivo,(int(pts1[x][0]),int(pts1[x][1])),5,(255,0,0),cv2.FILLED)

cv2.imshow('Cartas',archivo)
cv2.imshow('Perspectiva',archivo_salida)

cv2.waitKey(0)
