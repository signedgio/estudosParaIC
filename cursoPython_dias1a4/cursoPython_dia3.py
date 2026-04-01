# condicionais:

x = 2
y = 9

if not(x == y):
    print("Os valores são diferentes.")

# operadores de identidade:
## identificam se objetos estão na mesma localização de memória

objeto1 = {
    "bg": "Beomgyu",
    "sb": "Soobin"
}

objeto2 = {
    "bg": "Beomgyu",
    "sb": "Soobin"
}

if objeto1 is objeto2:
    print("'objeto1' e 'objeto2' estão localizados no mesmo local!")
else:
    print("'objeto1' e 'objeto2' estão localizados em locais diferentes!!!")

print(id(objeto1))
print(id(objeto2))

## diferente dos conjuntos, ao criamos variáveis com a mesma string ou mesmo número, o computador 
## salva armazenamento e coloca o mesmo id.

a = "ABC"
b = "ABC"

print(id(a))
print(id(b))

if a is b:
    print("a é b!")

if a is not b:
    print("a não é b!")


################################################################################################################################################################################################

# estruturas de repetição:

pessoas = ["Soobin", "Yeonjun", "Beomgyu", "Taehyun", "Kai"]

for pessoa in pessoas:
    print(pessoa) # isso imprime todas as pessoas da lista, na ordem em que foram colocadas

for pessoa in pessoas:
    if pessoa == "Beomgyu":
        break # isso faz com que o código verifique se a pessoa escolhida existe na lista. se sim, pare. ele vai imprimir apenas as pessoas que aparecem antes da pessoa selecionada. 
    print(f"Pessoa atual: {pessoa}")

for pessoa in pessoas:
    if pessoa == "Yeonjun":
        continue # isso faz com que o código verifique se a pessoa escolhida existe na lista. se sim, continue. ele pula a pessoa e continua a imprimir as outras pessoas presentes na lista.
    print(f"Pessoa atual: {pessoa}")

# usando range:

numeros = list(range(0, 11))
print(numeros)

for numero in range(5): # isso aqui imprime apenas 5 números (0 a 4)
    print(numero) 

for numero in range(0, 11): # isso aqui deixa bem claro que quer uma lista de 0 a 10
    print(numero)

for numero in range(len(pessoas)):
    print(pessoas[numero]) # explicação em baixo:

'''
tradução: para cada posição da lista pessoas, imprime o elemento daquela posição.
esse código funciona da mesma maneira que esse aqui:
for pessoa in pessoas:
    print(pessoa)
mas nesse caso, ele pega o número (posição) e fala pro código ir imprimindo cada nome em cada posição. o len da lista 
pessoas retorna a quantidade de pessoas presente no código (3, nesse caso).
em seguida, ele diz pra imprimir a lista pessoas em cada posição de cada número.
uma BOSTA de código
'''

# while:

contador = 0

while contador < 10:
    print(f"contagem: {contador}")
    contador += 1

########################################################################################################################################################################################
from functools import reduce ## isso aqui é pra usar nas funções de ordem maior! é pra poder usar o reduce.
# funções:

### seuNome = input("Digite o seu nome: ")

def cumprimentar(nome = "Laura"): # criando uma função
    print(f"Olá, {nome}! :)")

cumprimentar("Gio") # rodando a função
cumprimentar() # como especificamos o nome "Laura" lá em cima, caso nn tenha um parâmtero dentro desses parênteses, será impresso o que foi colocado quando a função foi criada!
### cumprimentar(seuNome)

def somar(num1, num2):
    total = num1 + num2
    print("O total é:", total)
    # return total

somar(8, 10)

# lambda:
## lambdas são como funções. elas são criadas de maneira mais rápida e só tem UMA expressão!!!
multiplicar = lambda num1, num2: num1 * num2
print(multiplicar(2, 5))

# funções de ordem maior:
# map:

lista1 = [1, 2, 3, 4, 5]

def duplicarLista(lista):
    listaDuplicada = []
    for numero in lista:
        listaDuplicada.append(numero * 2)
    return listaDuplicada
"""
traduzindo o que acontece aqui: 
criamos a função duplicarLista, que recebe como parâmetro a palavra lista, que vai ser definida quando chamarmos a função.
a partir da linha 128, criamos o que a função faz:
* criar uma nova lista chamada listaDuplicada; 
* dizer que, quando a função for chamada, já com seus parâmetros (lista), os valores colocados serão multiplicados por 2 e jogados para a lista listaDuplicada;
* retornar a lista, agora preenchida.
"""
lista2 = duplicarLista(lista1)
print(lista2)
'''
aqui foi criada uma nova lista e vemos que o parâmtro usado foi a lista 1.
então, os valores adicionados na listaDuplicada serão os valores da lista 1 multiplicados por 2.
'''

def duplicar(x):
    return x*2

lista_duplicada = list(map(duplicar, lista1))
print(lista_duplicada)

'''
aqui temos um código que faz exatamente a mesma coisa, mas de maneira muito mais rápida e que deixa o código MUITO MENOR!
o que acontece nesse caso:
criamos a função duplicar e definimos que sua função é duplicar o valor do parâmetro por 2;
embaixo criamos a variável lista_duplicada. nela, chamamos a função list(), que vai criar uma lista; 
depois chamamos a função map(), que mapeia todos os itens da lista e aplica a função em todos eles;
finalizando, definimos que ele deve mapear a lista 1 e aplicar a função duplicar em cada um dos itens da lista.

existe uma maneira ainda mais otimizada, que é usando lambda. nesse caso:
lista_duplicada = list(map(lambda x: x*2, lista1))
print(lista_duplicada)
'''

# filter:

def filtrarLista(lista):
    listaFiltrada = []
    for numero in lista:
        if numero % 2 == 0: # se o resto do número ao ser dividido por 2 for 0...
            listaFiltrada.append(numero)
    return listaFiltrada

listaNova = filtrarLista(lista1)
print(listaNova)


def filtro(x):
    return x % 2 == 0
    
lista2 = list(filter(filtro, lista1))
print(lista2)
##filter filtra dentro de uma lista os valores que seguem o parâmetro da função, que resultam como True.
## nesse caso, ele imprime os valores 2 e 4, que são os valores que tem seu resto 0.

lista3 = list(filter(lambda x: x % 2 == 0, lista1))
print(lista3)

# reduce: 
## pega uma lista e reduz tudo a um único valor!
## pega dois → junta → pega o resultado → junta com o próximo → repete

def somarLista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

somaDaLista = somarLista(lista1)
print(somaDaLista)

def somar(x, y):
    return x + y

soma = reduce(somar, lista1) # como ele devolve apenas um resultado, nn precisa colocar o list, já que nn vamos criar uma lista
print(soma)

somaDaLista = reduce(lambda x, y: x + y, lista1) 
print(somaDaLista)

