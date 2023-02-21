import cv2 as cv

img = cv.imread("Endereço da imagem/imagem.extenção")
cv.imshow("Imagem Original", img)

cv.waitKey(0)
cv.destroyAllWindows()