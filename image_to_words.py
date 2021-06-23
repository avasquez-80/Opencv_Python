#from _typeshed import SupportsItemAccess
import cv2
import pytesseract

img = cv2.imread('./archivos/textostring.png')
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

#while True:
#succes, img = cap.read()
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Detect Words
h_img, w_img, _ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits' #parametros indicados en el manual OEM PSM
boxes = pytesseract.image_to_data(img,config=conf) # se agrega la configuracion pytesseract para mostrar solo numeros
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
            cv2.putText(img,b[11],(x,y-7),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
cv2.imshow('Texto',img)
#if cv2.waitKey(1) == ord('x'):
#    break
cv2.imshow('Foto',img)
cv2.waitKey(0)
#cap.release()
#cv2.destroyAllWindows