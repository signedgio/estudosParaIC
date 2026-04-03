import cv2 as cv

imagem = cv.imread("fotos/beomgyu.jpg")
cv.imshow("BG!", imagem)

## CONVERTENDO UMA IMAGEM PARA CINZA:

cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
cv.imshow("cinza", cinza)

## USANDO EDGE CASCADE COM CANNY (cascade é um detector!!!):

contorno = cv.Canny(imagem, 125, 175)
# canny = os números definem o quão forte uma borda precisa ser para ser detectada.
cv.imshow("Contorno", contorno)

"""
| intensidade da borda |        resultado        |
| -------------------- | ----------------------- |
| < 125                | não tem borda! ignora.  | -> não vai ter borda nenhuma
| entre 125 e 175      | talvez tenha borda.     | -> borda mediana, nem muito forte, nem muito fraca
| > 175                | tem borda COM CERTEZA!  | -> borda FORTE

"""

# essa linha aqui em baixo pega as imagens do canny (só com bordas) e encontra os contornos das bordas.
contornos, hierarquia = cv.findContours(contorno, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# hierarquias: guardam quais contornos estão dentro de outros, os tratando com hierarquia mesmo! explico mais em baixo.
# cv.findContours: procura linhas fechadas e transforma elas em objetos
# cv.RETR_LIST: pega todos os contornos, sem se importar com a hierarquia
# cv.CHAIN_APPROX_NONE: guarda todos os pontos dos contornos
print(f"{len(contornos)} contornos encontrados!")

"""
hierarquias:
um quadrado grande
   dentro dele → um círculo
       dentro dele → outro círculo menor

o que temos aqui:
contorno 0 → quadrado (pai)
contorno 1 → círculo (filho)
contorno 2 → bolinha (vizinho (após o primeiro filho))

hierarquia[i] = [next, previous, child, parent]
| posição  | significado          |
| -------- | -------------------- |
| next     | próximo contorno     |
| previous | contorno anterior    |
| child    | contorno dentro dele |
| parent   | contorno que envolve |
"""

## BLUR:

blur = cv.GaussianBlur(cinza, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blurred bg", blur)
contornoDoBlur = cv.Canny(blur, 125, 175)
cv.imshow("contorno do blur", contornoDoBlur)

## RET E THRESH:

ret, thresh = cv.threshold(cinza, 125, 255, cv.THRESH_BINARY)
# essa linha transforma uma imagem em preto e branco PURO
# cv.threshold: ele separa a imagem em duas cores: preto e branco. ele decide quais pixeis são claros e quais são escuros baseado nos números.
# ret: o valor 125.
# thresh: quem devolve a imagem que foi feita
# 125, 255: 125 é o ponto de decisão! (menor que 125 retorna preto e maior ou igual retorna branco)
# cv.THRESH_BINARY: dita que é pra usar preto ou branco (nada no meio)
cv.imshow("thresh", thresh)

"""
diferença entre cv.threshold e cv.THRESH_BINARY:
threshold é a função (quem faz o trabalho), enquanto o THRESH_BINARY é o modo que o trabalho é feito.
threshold → “executa”
THRESH_BINARY → “como executar”

exemplo:
microondas(esquentar, 2 minutos, potência alta)
microondas → função
potência alta → modo
"""

cv.waitKey(0)