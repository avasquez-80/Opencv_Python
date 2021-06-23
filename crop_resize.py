import cv2

img = cv2.imread('./archivos/road.jpg')

width, height = 600,600

img_resize = cv2.resize(img,(width,height))
print(f'El ancho de la imagen es {width} y el ancho de la imagen es {height}')

img_crop = img_resize[300:600,:600]

cv2.imshow('Resize', img_resize)
cv2.imshow('Crop', img_crop)
cv2.waitKey(0)