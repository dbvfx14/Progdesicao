'''Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.'''

num1 = float(input("Informe um numero número: "))
num2 = float(input("Informe outro número: "))

if num1 > num2:
    print(f"O maior número é {num1} e o menor número é {num2}.")
elif num2 > num1:
    print(f"O maior número é {num2} e o menor número é {num1}.")
else:
    print("Os dois números são iguais.")