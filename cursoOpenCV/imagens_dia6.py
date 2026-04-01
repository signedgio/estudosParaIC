import cv2 as cv

## LENDO IMAGENS:

imagem = cv.imread("fotos/florbonita.jpg")
cv.imshow("Flor!", imagem)
cv.waitKey(0) # essa waitKey(0) significa: mostra a imagem e espera até o usuário apertar alguma tecla.
# caso fosse cv.waitKey(1), levaria 1 milissegundo para aparecer algo na tela e ela fecharia rapidamente.
