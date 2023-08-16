'''Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, entre 5001 e 8000, ou acima de 8000.'''

num = int(input("Informe um número: "))

if num < 1000:
    print("O número está abaixo de 1000.")
if num <= 5000:
    print("O número está entre 1000 e 5000.")
if num <= 8000:
    print("O numero esta entre 5001 e 8000.")
else:
    print("O numero esta a cima de 8000.")