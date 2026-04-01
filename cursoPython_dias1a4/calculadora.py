print("== CALCULADORA ==")
print("-----------------")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
tipoDeSol = input("Digite o tipo de solução que deseja realizar (entre soma, subtração, multiplicação e divisão): ")

if tipoDeSol == "Soma":
    print("Resultado: ", num1 + num2)
elif tipoDeSol == "Subtração":
    print("Resultado: ", num1 - num2)
elif tipoDeSol == "Multiplicação":
    print("Resultado: ", num1*num2)
elif tipoDeSol == "Divisão":
    print("Resultado: ", num1/num2)
else:
    print("Erro! Tente novamente.")