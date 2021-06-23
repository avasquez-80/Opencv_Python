import cv2
from face_recognition.api import face_distance
import numpy as np
import face_recognition

img_elon = face_recognition.load_image_file('/home/alejandro/Proyectos/ProyectosNuevos/Python/practicas/opencv/practicas/data/elon-musk.jpg')
img_elon = cv2.cvtColor(img_elon,cv2.COLOR_BGR2RGB)
img_test = face_recognition.load_image_file('/home/alejandro/Proyectos/ProyectosNuevos/Python/practicas/opencv/practicas/data/bill_gates.jpg')
img_test = cv2.cvtColor(img_test,cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(img_elon)[0]
encode_elon = face_recognition.face_encodings(img_elon)[0]

face_loc_test = face_recognition.face_locations(img_test)[0]
ecode_test = face_recognition.face_encodings(img_test)[0]

cv2.rectangle(img_elon,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(0,255,0),3)
cv2.rectangle(img_test,(face_loc_test[3],face_loc_test[0]),(face_loc_test[1],face_loc_test[2]),(0,255,0),3)

results = face_recognition.compare_faces([encode_elon],ecode_test)
distance = face_recognition.face_distance([encode_elon],ecode_test)

print(results,distance)
cv2.putText(img_test,f'{results} {round(distance[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),3)
#cv2.imshow('Elion',img_elon)
cv2.imshow('Test',img_test)

cv2.waitKey(0)