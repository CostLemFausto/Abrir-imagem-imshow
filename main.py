#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Este software garrega uma imagem na tela, mostra no terminal
# sua  dimensão em pixels, e também pode redimensionar a mesma
#*************************************************************
import cv2 as cv

img = cv.imread("Endereço da imagem/imagem.extenção")
def dimensao():
    pass

cv.imshow("Imagem Original", img)

cv.waitKey(0)
cv.destroyAllWindows()