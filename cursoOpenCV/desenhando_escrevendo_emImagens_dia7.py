import cv2 as cv
import numpy as np

## DESENHNADO EM IMAGENS:

img = cv.imread("fotos/florbonita.jpg")
cv.imshow("Flor", img)
telaParaDesenhar = np.zeros((500, 500, 3), dtype = "uint8")
# cria uma imagem de 500x500 com 3 cores, onde todos os pixels têm valor 0 (preto), usando números de 0 a 255.
# np.zeros() = cria uma matriz cheia de zeros.
# dtype = tipo de número que eu quero usar.
# uint8 = números vão de 0 a 255. 0 = preto, 255 = branco, valores no meio = tons de cinza.
cv.imshow("Tela", telaParaDesenhar)

# pintando a tela de verde:
telaParaDesenhar[:] = 0, 255, 0
# [:] = pinta a imagem INTEIRA com essa cor!
# (B, G, R) = 0, 255, 0
cv.imshow("Tela verde", telaParaDesenhar)

# pintando apenas uma parte da tela de vermelho:
telaParaDesenhar[200:300, 300:400] = 0, 0, 255
cv.imshow("Tela com uma pitadinha de vermelho", telaParaDesenhar)


"""
na hora de pintar, eu tive um erro interessante.
na linha 16, temos esse código: telaParaDesenhar[:] = 0, 255, 0
ao tentar pintar apenas uma parte da tela de verde na linha 22, não funcionou, porque a tela inteira estava verde.
isso acontece porque o código apenas pega essa imagem inicialmente modifica e a modifica novamente. ela não volta ao preto original definido lá em cima. 
"""

# desenhando um retângulo:
cv.rectangle(telaParaDesenhar, (0,0), (250,250), (255, 0, 0), thickness = 2)
            # tela, origem do retangulo, final do retangulo, cor, grossura do triangulo.
cv.imshow("Retangulo", telaParaDesenhar)

# preenchendo o retangulo com cor:
cv.rectangle(telaParaDesenhar, (0,0), (250,250), (255, 0, 0), thickness = cv.FILLED)
cv.imshow("Retangulo preenchido", telaParaDesenhar)

# desenhando um círculo (criei uma tela do zero pra facilitar):
telaNova = np.zeros((500, 500, 3), dtype = "uint8") 
cv.circle(telaNova, (250,250), 40, (255, 0, 0), thickness = 3)
        # tela, centro, raio, cor, grossura.
cv.imshow("Tela com um círculo", telaNova)

# desenhando uma linha:
cv.line(telaNova, (0,0), (250,250), (255, 255, 255), thickness = 2)
cv.imshow("Tela com um círculo e uma linha", telaNova)

## ESCREVENDO EM IMAGENS:
cv.putText(telaNova, "Oieeeee!", (225, 225), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), thickness = 2)
          # tela, texto a aparecer, ponto, fonte, tamanho, cor, grossura
cv.imshow("Texto", telaNova)
cv.waitKey(0)



