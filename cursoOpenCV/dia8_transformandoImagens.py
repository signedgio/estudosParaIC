import cv2 as cv
import numpy as np

imagem = cv.imread("fotos/morcegosFloridos.jpg")
cv.imshow("Imagem normal", imagem)

## TRADUZINDO UMA IMAGEM (mexendo uma imagem nos eixos x e y):
def traduzir(imagem, x, y):
    # cria a funçõs traduzir que recebe como parâmetros a imagem que vamos modificar, quanto mover no eixo x e quanto mover no eixo y.
    movimentandoImagemNaMatriz = np.float32([[1, 0, x], 
                                  [0, 1, y]])
                          # explica como mover a imagem. define a variável, explica pro código que os números são float (np.float32), define onde mexer x e y.
    dimensoes = (imagem.shape[0], imagem.shape[1])
                 # altura [0] e largura [1]
    return cv.warpAffine(imagem, movimentandoImagemNaMatriz, dimensoes)
    # esse cv.warpAffine é quem executa as mudanças na matriz!
"""
como funcionam os eixos da matriz em open cv:
(0,0) ───────→ x positivo
  │
  │
  ↓ y positivo

descer (y) = positivo
subir (y) = negativo
eles andam, de padrão, pra direita e pra baixo!!!!!!
precisamos lembrar que os [1, 0] e [0, 1] ates de x e y continuam SEMPRE nessa mesma posição! a única coisa que muda são os valores de x e y!!!!

[ 1  0  1 ]
[ 0  1  0 ]
(x=1, y=0) aqui x move 1 pixel pra direita e y faz nada

[ 1  0  0 ]
[ 0  1  1 ]
(x=0, y=1) aqui y move 1 pixel pra baixo e x faz nada

[ 1  0  -3 ]
[ 0  1  -2 ]
(x = -3, y = -2) aqui x move 3 pixels pra esquerda e y sobe dois pixels
"""
imagemTraduzida = traduzir(imagem, -100, 100)
cv.imshow("morcegos traduzidos", imagemTraduzida)


## ROTAÇÃO DE IMAGENS:

def rotacionando(imagem, angulo, pontoDeRotacao = None):
    (altura, largura) = imagem.shape[:2]
                        # pega até o segundo íncia da lista [altura, largura, BRG]
    if pontoDeRotacao is None:
        pontoDeRotacao = (largura//2, altura//2)
                         # tem que ser nessa ordem pq x = largura e y = altura!!! 
        # isso aqui diz pro código que, caso nn sejam enviados os pontos, ele deve girar no CENTRO da imagem.
        rotacionandoImagemNaMatriz = cv.getRotationMatrix2D(pontoDeRotacao, angulo, 1.0)
                                     # quem cria o plano de rotação, variável, angulo de rotação e escala (zoom)
        dimensoes = (largura, altura)
        # se coloca esse dimensoes aqui pra ser executado no warpAffine, pra definir o tamanho da imagem final.
        return cv.warpAffine(imagem, rotacionandoImagemNaMatriz, dimensoes)
        # return com cv.warpAffine pra devolver a imagem rotaciona pq é ele quem executa as mudanças na matriz
"""
escalas:
1.0 → tamanho normal
2.0 → aumenta
0.5 → diminui
"""

imagemRotacionada = rotacionando(imagem, 45)
                                         # angulo que queremos que a imagem rotacione  
cv.imshow("morcegos rotacionados", imagemRotacionada)


## ARRUMANDO O TAMANHO DE UMA IMAGEM:

resized = cv.resize(imagem, (500,500), interpolation = cv.INTER_AREA)
cv.imshow("Diminuida", resized)

## VIRANDO UMA IMAGEM:

flip = cv.flip(imagem, 1)
cv.imshow("flip", flip)

"""
tipos de flip:
0 - virar uma imagem verticalmente
1 - virar uma imagem horizontalmente
-1 - virar uma imagem tanto verticalmente, quanto horizontalmente
"""

## CORTANDO UMA IMAGEM:

cropped = imagem[200:400, 200:300]
cv.imshow("cortada", cropped)

cv.waitKey(0)

