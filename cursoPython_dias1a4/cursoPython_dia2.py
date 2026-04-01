# listas:
frutas = ["Uva", "Banana", "Lichia"]
print(frutas)

frutas.append("Melancia") # append adiciona algo a uma lista existente
frutas.remove("Uva")
frutas.reverse() # reverse inverte a ordem de uma lista
frutas.sort() # sort deixa uma lista em ordem alfabética
frutas.sort(reverse=True) # nesse caso, será colocado em ordem alfabética reversa              

# mexendo numa lista a partir de posições:
frutas.insert(2, "Mexerica") # insert permite que você insira um item em uma posição específica da lista!
frutas[0] = "Banana nanica" # assim alteramos o valor de um item na posição escolhida
frutas.pop(2) # isso aqui remove o item de uma lista de acordo com a sua posição

#####################################################################################################

# tuplas:
## tupla é como uma lista de vários itens, mas seus itens são IMUTÁVEIS!
## assim como uma lista, é possível utilizar funções para encontrar um item por sua posição e usar o len!

cores = ("preto", "roxo", "azul")
corQueNaoGosto = ("laranja",) # para criar uma tupla com um único item, é necessário colocar uma vírgula 

del corQueNaoGosto # isso deleta uma tupla

#####################################################################################################

# conjuntos:
## como uma lista e tupla, mas não é possível localizar um item por sua posição e não aceita itens duplicados!
## len e del funcionam aqui do mesmo jeito como nos outros

idiomas = {"Português BR", "Mandarim", "Inglês"}
print("Inglês" in idiomas) # aqui é uma caso em que retorna True ou False no terminal

idiomas.add("Coreano")
idiomas.remove("Inglês")
idiomas.clear() # remove todos os itens de um conjunto (saída: set())

######################################################################################################

# dicionários:
## clear, len e pop funcionam aqui da mesma maneira

pessoa = {
    "nome": "Beomgyu",
    "sobrenome": "Choi",
    "idade": 25
}

# maneiras de acessar dados de um dicionário:
print(pessoa["nome"])
pessoa.get("sobrenome")

# adicionando propriedades a um dicionário:
pessoa["nacionalidade"] = "Coreano"

# imprimindo as partes de um dicionário:
print(pessoa.keys())
print(pessoa.items())

#copiando um dicionário para outro, mudando seu conteúdo e adicionando propriedades:
ursoHumano = pessoa.copy()
print(ursoHumano)
ursoHumano["nome"] = "Soobin"
ursoHumano["cidade natal"] = "Ansan"

# removendo um item de um dicionário:
del(pessoa["idade"])
pessoa.pop("idade")

# BONUS:
## criando uma lista de dicionários!!!

pessoas = [
    {"nome": "Choi Beomgyu", "idade": 25},
    {"nome": "Choi Soobin", "idade": 25}
]

print(pessoas[1]["nome"]) # isso imprime o nome da segunda pessoa do dicionário
