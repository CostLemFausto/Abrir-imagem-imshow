# Abrir-imagem-imshow
Este software abre uma imagem na tela utilizando a função "imshow"
do opencv-python.

import cv2 as cv -> Importa a bibiloteca opencv, e a apelida de cv.

img = cv.imread("Endereço da imagem/imagem.extenção") -> Lê a imagem no endereço contido entre parênteses e aspas, e a deposita na variável img.

cv.imshow("Imagem Original", img) -> Exibe a imagem.

cv.waitKey(0) -> Aguarda a imagem ser exibida.
cv.destroyAllWindows() -> Fecha todas as janelas após cessar a exibição da imagem.