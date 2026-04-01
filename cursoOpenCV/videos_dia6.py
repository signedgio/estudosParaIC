import cv2 as cv

## LENDO VÍDEOS:

"""
cv.VideoCapture(0)  # câmera do notebook
cv.VideoCapture(1)  # outra câmera (se tiver)
cv.VideoCapture("video.mp4")  # abre um vídeo
"""

video = cv.VideoCapture("vídeos/videoteste.mp4")

while True:
    isTrue, frame = video.read()
    # isTrue = se deu certo
    cv.imshow("Video!", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    ## se eu apertar a tecla d, pare o vídeo. break para o loop.
"""
explicando:
repita pra sempre:
se deu certo, pega o vídeo atual e vai lendo frame por frame (capture.read)
abre a janela Vídeo! com o vídeo escolhido (frame)
colocamos um tempo de 20 milli e colocamos esse 0xFF pra pegar o valor certo da tecla definida na frente como o botão de "pare" do vídeo. 
se ela for apertada, pare o vídeo. 
break.
"""
    
video.release() # desliga a câmera
cv.destroyAllWindows() # fecha a janela do vídeo

