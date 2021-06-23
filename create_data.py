import cv2
import os
import time

##########################################################################
my_path = 'data/images'
camera_no = 0
camera_bridghtness = 180
module_val = 10     #save every 1th frame to avoid repetition
min_blur = 500      #smaller value means more blurriness present
gray_image = False
save_data = True
show_image = True
img_width = 180
img_height = 120
##########################################################################

global count_folder
cap = cv2.VideoCapture(camera_no)
cap.set(3,640)
cap.set(4,480)
cap.set(10,camera_bridghtness)

count = 0
count_save = 0

def save_data_func():
    global count_folder
    count_folder = 0
    while os.path.exists(my_path + str(count_folder)):
        count_folder +=1
    os.makedirs(my_path + str(count_folder))

if save_data:save_data_func()

while True:
    succes,img = cap.read()
    img = cv2.resize(img,(img_width,img_height))
    if gray_image:img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if save_data:
        blur = cv2.Laplacian(img,cv2.CV_64F).var()
        if count % module_val == 0 and blur > min_blur:
            now_time = time.time()
            cv2.imwrite(my_path + str(count_folder) + '/' + str(count_save) + '_' + str(int(blur)) + "_" + str(now_time) + '.png',img)
            count_save +=1
        count +=1
    if show_image:
        cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows