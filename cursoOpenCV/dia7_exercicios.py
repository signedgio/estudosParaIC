"""
EXERCÍCIO 1 — Resize inteligente

👉 pega uma imagem e:

diminui ela usando cv.INTER_AREA
aumenta ela usando cv.INTER_CUBIC
mostra as duas

💡 objetivo: ver a diferença
"""
import cv2 as cv

imagem = cv.imread("fotos/morcegosFloridos.jpg")
cv.imshow("Imagem normal", imagem)

diminuirImagem = cv.resize(imagem, (200,200), interpolation = cv.INTER_AREA)
cv.imshow("Imagem menor", diminuirImagem)

aumentarImagem = cv.resize(imagem, (750,750), interpolation = cv.INTER_CUBIC)
cv.imshow("Imagem maior", aumentarImagem)


"""
🟡 EXERCÍCIO 2 — Testando blur

👉 pega uma imagem e cria:

blur com (3,3)
blur com (7,7)
blur com (15,15)

👉 mostra todos

💡 objetivo: entender intensidade
"""

blur1 = cv.GaussianBlur(imagem, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur menor", blur1)

blur2 = cv.GaussianBlur(imagem, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur mediano", blur2)

blur3 = cv.GaussianBlur(imagem, (15,15), cv.BORDER_DEFAULT)
cv.imshow("Blur forte", blur3)

"""
🔵 EXERCÍCIO 3 — Canny na prática

👉 usa:

cv.Canny(imagem, 50, 100)
cv.Canny(imagem, 100, 200)
cv.Canny(imagem, 150, 300)

👉 mostra os 3 resultados

💡 objetivo: ver como os thresholds mudam tudo
"""

bordas = cv.Canny(imagem, 50, 100)
cv.imshow("Bordas sutis", bordas)
bordas = cv.Canny(imagem, 100, 200)
cv.imshow("Bordas medianas", bordas)
bordas = cv.Canny(imagem, 150, 300)
cv.imshow("Bordas fortes", bordas)


"""
🟣 EXERCÍCIO 4 — Dilate vs Erode

👉 faz isso:

aplica Canny
aplica dilate (iterations=2)
aplica erode

👉 mostra os 3

💡 objetivo: ver “engrossar vs afinar”
"""

canny2 = cv.Canny(imagem, 125, 175)
dilatar = cv.dilate(canny2, (3,3), iterations=2)
cv.imshow("Imagem dilatada", dilatar)
afinar = cv.erode(canny2, (3,3), iterations=1)
cv.imshow("Imagem afinada", afinar)


"""
🔴 EXERCÍCIO 5 — Desenho completo

👉 cria uma tela preta e:

desenha um retângulo
desenha um círculo
escreve um texto

💡 objetivo: juntar tudo que você aprendeu
"""
import numpy as np

tela = np.zeros((500, 500, 3), dtype = "uint8")
cv.imshow("Tela", tela)

retangulo = cv.rectangle(tela, (55, 55), (300,300), (255, 0, 0), thickness = 2)
cv.imshow("Tela + rectangle", retangulo)

circulo = cv.circle(tela, (250, 250), 80, (255, 0, 0), thickness = 5)
cv.imshow("Tela + rectangle + circle", circulo)

texto = cv.putText(tela, "Oie! To fazendo exercícios. :)", (95, 95), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255), thickness = 1)
# tela, texto a aparecer, ponto, fonte, tamanho, cor, grossura
cv.imshow("Tela + rectangle + circle + texto", texto)


cv.waitKey(0)

