import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('./archivos/barras1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('./archivos/my_data_file.txt') as f:
    my_data_list = f.read().splitlines()
#print(my_data_list)
while True:
    succes,img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        my_data = barcode.data.decode('utf-8')
        #print(my_data)
        pts2 = barcode.rect
        if my_data in my_data_list:
            #print('Autorizado')
            color = (0,255,0)
            estado = 'Autorizado'
        else:
            #print('No autorizado')
            color = (0,0,255)
            estado = 'No autorizado'
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,color,5)
        #cv2.putText(img,my_data,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,color,2)
        cv2.putText(img,estado,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,color,2)
    cv2.imshow('Resultado',img)
    if  cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows