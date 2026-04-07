import cv2 as cv

bg = cv.imread("fotos/beomgyuDeFrente.jpg")
cv.imshow("BG!", bg)

cinza = cv.cvtColor(bg, cv.COLOR_BGR2GRAY)
cv.imshow("BG cinza", cinza)

haarCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
# criamos uma variável que carrega o arquivo .xml que detecta rostos!
# cv.CascadeClassifier: quem lê as 34 mil linhas de código do .xml 

retanguloRostos = haarCascade.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=3)
# essa linha funciona para dectar os rostos.
# detectMultiScale: é quem analiza a imagem, procura padrões nos rostos e retorna posições! explicação abaixo. 
# colocamos a imagem em cinza pois é mais fácil de detectar
# scaleFactor = 1.1: controla como o dectectMultiScale procura rostos em diferentes tamanhos! esse 1.1 é pra ir reduzindo o tamamho da busca aos poucos.
# minNeighbors=3: controla quantas vezes algo precisa parecer um rosto pra ser considerado um rosto
print(f"Numero de rostos encontrados: {len(retanguloRostos)}")

"""
* detectMultiScale retorna: 
[(x, y, w, h), (x, y, w, h)]

👉 cada tupla = um rosto encontrado

x, y → posição
w, h → tamanho

* scaleFactor: como se procuram os rostos
| valor | comportamento               |
| ----- | --------------------------- |
| 1.05  | mais preciso (mais lento)   |
| 1.1   | equilíbrio                  |
| 1.3   | mais rápido (menos preciso) |

* minNeighbors: o quão exigente é a procura por rostos

| valor | comportamento                  |
| ----- | ------------------------------ |
| 3     | mais detecções (pode dar erro) |
| 5     | mais confiável                 |
| 8     | muito rígido                   |
"""

# desenhando os retângulos pra valer:
for (x,y,w,h) in retanguloRostos:
    cv.rectangle(bg, (x,y), (x+w, y+h), (255,0,0), thickness = 2)
              # imagem, ponto1 (onde começa), ponto2 (onde termina), cor, grossura

cv.imshow("Rosto detectado", bg)

"""
| variável | significado       |
| -------- | ----------------- |
| `x`      | começo horizontal |
| `y`      | começo vertical   |
| `w`      | largura do rosto  |
| `h`      | altura do rosto   |


(x, y) = começo

    ●──────────●
    │          │
    │  rosto   │
    │          │
    ●──────────●
           (x+w, y+h)


“se começa em x e tem largura w…”
final em x = x + w

“se começa em y e tem altura h…”
final em y = y + h

x = 10
y = 20
w = 30
h = 40

começo:
(10, 20)

final:
(10+30, 20+40) = (40, 60)

"""

txt = cv.imread("fotos/txt3.jpg")
txtCinza = cv.cvtColor(txt, cv.COLOR_BGR2GRAY)
cv.imshow("TXT!", txtCinza)

retanguloRostos = haarCascade.detectMultiScale(txtCinza, scaleFactor=1.1, minNeighbors=3)
print(f"Numero de rostos encontrados: {len(retanguloRostos)}")

for (x,y,w,h) in retanguloRostos:
    cv.rectangle(txt, (x,y), (x+w, y+h), (255,0,0), thickness = 1)

cv.imshow("Rostos detectados", txt)








cv.waitKey(0)