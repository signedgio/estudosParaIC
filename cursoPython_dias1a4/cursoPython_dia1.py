# para descobrir o tipo de uma variável, podemos utilizar a função "type()"

x = 10
y= 2.5
z = "Ebaaaaaaaaa!"
blablabla = True

print(type(x))
print(type(y))          
print(type(z))
print(type(blablabla))

# deixando um programa menor transformando várias linhas compostas por variáveis em uma única linha:

x, y, z, blablabla = (10, 2.5, "Ebaaaaaaaaa!", True)
print(x)
print(y)
print(z)
print(blablabla)

# tipos de utilização de divisões:

print(7//2) # imprime o resultado da divisão com apenas uma casa decimal
print(7 % 2) # imprime o resto da divisão

# tipos de utilização de multiplicações:

print(3**4) # imprime a potência 

# outra coisa:

a = 5
a += 1
print(a)

b = 2
b -= 1
print(b)

c = 7
c *= 2
print(c)

d = 9
d /= 3
print(d)

# combinando strings:

nome = "Giovanna"
idade = 18

mensagem1 = "Olá, meu nome é " + nome + ". Eu tenho " + str(idade) + " anos." # str() converte número em string:
print(mensagem1)

mensagem2 = "Olá, meu nome é {a}. Eu tenho {b} anos.".format(a=nome, b=idade)
print(mensagem2)

mensagem3= f"Olá! Meu nome é {nome}. Eu tenho {idade} anos e estou cursando Engenharia Mecatrônica na FAIP!"
print(mensagem3)

# métodos de strings:

frase1 = "olá, mundo! :)"
print(frase1.capitalize()) # deixa a primeira letra da frase maiúscula
print(frase1.upper()) # deixa todas as letras da frase maiúsculas

frase2 = "TXT 4TH GEN LEADERS!!!"
print(frase2.lower()) # deixa todas as letras da frase minúsculas   
print(frase2.replace("TXT", "ENHYPEN")) # substitui uma palavra por outra

frase3 = "Volta pro ENHYPEN, Heeseung :("
print(frase3.swapcase()) # troca as letras maiúsculas por minúsculas e vice-versa

print(len(frase1)) # conta o número de caracteres da frase, incluindo os espaços
print(len(frase2))
print(len(frase3))
# o len funciona para listas também, dessa mesma maneira

letra = "e"
print(frase3.count(letra)) # conta quantas vezes a letra "e" aparece na frase3

print(frase3.startswith("Volta")) # verifica se a frase3 começa com a palavra "Volta"
print(frase3.endswith(":(")) # verifica se a frase3 termina com a palavra ":("
print(frase3.find("ENHYPEN")) # verifica a posição da palavra "ENHYPEN" na frase3, caso a palavra não exista, retorna -1

print(frase3.split()) # separa a frase3 em uma lista de palavras, utilizando o espaço como separador
print(frase3.split(sep="E")) # separa a frase3 em uma lista de palavras, utilizando a letra "E" como separador

print(frase3.isalnum()) # verifica se a frase3 é composta apenas por letras e números. retorna False pois a frase3 contém espaços e caracteres especiais
print(frase3.isalpha()) # verifica se a frase3 é composta apenas por letras. retorna False pois a frase3 contém espaços e caracteres especiais
print(frase3.isnumeric()) # verifica se a frase3 é composta apenas por números. retorna False pois a frase3 contém letras, espaços e caracteres especiais

