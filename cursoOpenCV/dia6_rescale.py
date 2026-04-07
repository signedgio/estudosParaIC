import cv2 as cv

## MUDANDO O FORMATO DE ALGO:

# na hora de criar essa função aqui em baixo, temos de ter em mente que ela funcionará tanto para uma foto, quanto para um vídeo! isso porque, um vídeo são várias fotos juntas, vários frames!
def rescaleFrame(frame, scale=0.75): # criando uma função que aumenta ou diminui imagens. nesse caso, como temos 0,75, ele quer uma imagem MENOR!
    width = int(frame.shape[1] * scale) # frame.shape[] = qual o tamanho dessa imagem?
    height = int(frame.shape[0] * scale) # frame.shape[] funciona com três coisas naturais dele: frame.shape → (altura, largura, cores). os números colocados nos colchetes significam essas coisas!
    # esse scale é basciamente um "pega isso e diminui".
    dimensions = (width, height) # aqui se dá o novo tamanho da imagem
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # muda o tamanho da imagem pra esse novo tamanho e faz desse método aqui...
    # o interpolation é o método! como nesse caso é INTER_AREA, significa DIMINUIR a imagem

# essa função funciona para captura de vídeo (webcam), não para imagens nem vídeos já salvos
def mudarResolucao(width, height):
    video.set(3, width)
    video.set(4, height)
"""
diferente do caso do .shape(), o .set() funciona para acessar coisas específicas de um "menu". 
shape = uma lista. 
    lista = ["altura", "largura", "cores"] 
    frame.shape[0] → altura  
    frame.shape[1] → largura  
    frame.shape[2] → cores 
set = um "controle remoto", onde você escolhe uma configuração em específico para mudar.
    3 = largura  
    4 = altura  
    10 = brilho  
    11 = contraste  
"""

video = cv.VideoCapture("vídeos/videoteste.mp4")
imagem = cv.imread("fotos/florbonita.jpg")


while True:
    isTrue, frame = video.read() # o que acontece aqui:
    # loop 1 → frame = imagem do vídeo (momento 1)
    # loop 2 → frame = imagem do vídeo (momento 2)
    # loop 3 → frame = imagem do vídeo (momento 3)
    cv.imshow("Video!", frame)
    video_resized = rescaleFrame(frame) # isso aqui cria uma nova variável com o vídeo nu formaoto menor, com seu tamanho definidio pelo (frame), que foi definidio na função lá em cima.
    cv.imshow("Vídeo menorzinho :)!", video_resized)
    cv.imshow("Flor!", imagem) 
    imagem_resized = rescaleFrame(imagem) # não usamos "frame" aqui porque ele representa a imagem que vem do vídeo, enquanto "imagem" é a imagem carregada do arquivo.
    cv.imshow("Flor menorzinha! :)", imagem_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break