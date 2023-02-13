import cv2 as cv

img = cv.imread("/home/takion/Documentos/Pixel/Fausto.jpeg")
cv.imshow("Imagem Original", img)

cv.waitKey(0)
cv.destroyAllWindows()