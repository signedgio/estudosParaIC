import cv2 as cv

imagem = cv.imread("fotos/florbonita.jpg")
cv.imshow("Flor!", imagem)

## CONVERTENDO UMA IMAGEM BGR PARA CINZA: 

cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
cv.imshow("Cinza", cinza)

# BLUR:

blur = cv.GaussianBlur(imagem, (3,3), cv.BORDER_DEFAULT)
# esse border default é só o jeito que o OpenCV lida com as bordas da imagem.
cv.imshow("flor com blur", blur)


"""
| valor   | efeito           |
| ------- | ---------------- |
| (3,3)   | blur leve        |
| (5,5)   | blur médio       |
| (9,9)   | blur forte       |
| (15,15) | MUITO borrado    |

"""

# USANDO EDGE CASCADE COM CANNY (cascade é um detector!!!):
contorno = cv.Canny(imagem, 125, 175)
# canny = os números definem o quão forte uma borda precisa ser para ser detectada.
cv.imshow("Contorno", contorno)
contorno = cv.Canny(blur, 125, 175)
cv.imshow("Contorno do blur", contorno)

"""
| intensidade da borda |        resultado        |
| -------------------- | ----------------------- |
| < 125                | não tem borda! ignora.  | -> não vai ter boarde nenhuma
| entre 125 e 175      | talvez tenha borda.     | -> borda mediana, nem muito forte, nem muito fraca
| > 175                | tem borda COM CERTEZA!  | -> borda FORTE

"""

# DILATANDO O CONTORNO DE UMA IMAGEM:

dilatar = cv.dilate(contorno, (3,3), iterations = 1)
                   # variável, efeito, quantidade de dilatações.
# dilatar = engrossar as bordas!
# iterations = quantas vezes a dilatação vai acontecer!!!
cv.imshow("dilatado", dilatar)

"""
definindo o efeito da dilatação:
| valor | efeito |
| ----- | ------ |
| (3,3) | leve   |
| (5,5) | médio  |
| (9,9) | forte  |

"""

## AFINANDO O CONTORNO DE UMA IMAGEM:

afinar = cv.erode(contorno, (3,3), iterations = 1)
cv.imshow("Afinado", afinar)


## MODIFICAR O TAMANHO DE UMA IMAGEM:

resize = cv.resize(imagem, (500,500), interpolation = cv.INTER_AREA) # muda o tamanho da imagem pra esse novo tamanho e faz desse método aqui...
# o interpolation é o método! como nesse caso é INTER_AREA, significa DIMINUIR a imagem
cv.imshow("MUDANÇA DE TAMANHO", resize)

"""
| Interpolation       | Quando usar                                    |
| ------------------- | ---------------------------------------------- |
| `cv.INTER_AREA`     | Diminuir imagem                                |
| `cv.INTER_LINEAR`   | Uso padrão (resize normal)                     |
| `cv.INTER_CUBIC`    | Aumentar imagem com mais qualidade             |
| `cv.INTER_NEAREST`  | Quando precisa ser rápido (aceitando pixelado) |
| `cv.INTER_LANCZOS4` | Aumentar imagem com alta qualidade             |
"""

## CORTANDO UMA IMAGEM:

cortada = imagem[50:200, 200:400]
        # definindo dentro dos colchetes os pontos que devem ser cortados da imagem
cv.imshow("Cortada", cortada)

cv.waitKey(0)