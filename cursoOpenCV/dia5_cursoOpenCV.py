import cv2 

# USANDO A O INPUT E LEITURA DA IMAGEM: 

imagemBulbassauro = cv2.imread(r"C:\Users\gioro\Downloads\bulbassauroFofinho.jpg")
x, y = imagemBulbassauro.shape[:2] ## esse [:2] é um método de fatiamento. ele funciona pra que o format imprima apenas duas de suas funções. 
print("Altura: {}, Largura = {}".format(x, y))
## esse format funciona de maneira que as chaves {} criam buracos no seu texto e são substituituídas pelos valores de x e y nesse caso.
## o formato funciona de maneira muita mais rápida do que a criação de variáveis.

(R, G, B) = imagemBulbassauro[250, 250] ## procurando o RGB da imagem nos exatos pontos x = 250 e y = 250
print("R = {}, G = {}, B = {}".format(R, G, B))

B = imagemBulbassauro[250, 250, 0]
print("Apenas o valor de B = {}".format(B))

# MUDANDO O TAMANHO DA IMAGEM E CRIANDO UM NOVO ARQUIVO:

tamanho = cv2.resize(imagemBulbassauro, (1920, 1080))
## mandando o computador salvar a foto 'tamanho' e me avisar (True) se conseguiu.
print(cv2.imwrite("imagem_do_bulba_ajustada.jpg", tamanho))

retangulo = cv2.rectangle(imagemBulbassauro, (1500, 900), (600, 400), (255, 0, 0), 2)