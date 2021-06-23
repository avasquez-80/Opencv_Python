import cv2
import pytesseract

img = cv2.imread('./archivos/textostring.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Detect Characters
h_img, w_img, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,h_img-y),(w,h_img-h),(0,0,255),3)
    cv2.putText(img,b[0],(x,h_img-y+25),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,(0,0,255),3)
cv2.imshow('Foto',img)
cv2.waitKey(0)