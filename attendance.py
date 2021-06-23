import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = '/home/alejandro/Proyectos/ProyectosNuevos/Python/practicas/opencv/practicas/image_attendance'
images = []
class_names = []
my_list = os.listdir(path)
print(my_list)
for cl in my_list:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    class_names.append(os.path.splitext(cl)[0]) #para remover el .jpg de los nombres
print(class_names)

#Funcion para realizar el encoding de las imagenes
def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return(encode_list)

def mark_attendance(name):
    with open('/home/alejandro/Proyectos/ProyectosNuevos/Python/practicas/opencv/practicas/attendance.csv','r+') as f:
        my_datalist = f.readlines()
        namelist=[]
        for line in my_datalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dt_string = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dt_string}')

encode_list_known = find_encodings(images)
#print(len(encode_list_known))
print('Encoding complete!')

cap = cv2.VideoCapture(0)

while True:
    succes,img = cap.read()
    img_s=cv2.resize(img,(0,0),None,0.25,0.25)
    img_s=cv2.cvtColor(img_s,cv2.COLOR_BGR2RGB)

    faces_cur_frame = face_recognition.face_locations(img_s)
    encoding_cur_frame = face_recognition.face_encodings(img_s,faces_cur_frame)

    for encode_face,face_loc in zip(encoding_cur_frame,faces_cur_frame):
        matches = face_recognition.compare_faces(encode_list_known,encode_face)
        face_dist = face_recognition.face_distance(encode_list_known,encode_face)
        #print(face_dist)
        match_index = np.argmin(face_dist)
        if matches[match_index]:
            name = class_names[match_index].upper()
            #print(name)
            y1,x2,y2,x1 = face_loc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
            mark_attendance(name)
    cv2.imshow('WebCam',img)
    if cv2.waitKey(1) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows
