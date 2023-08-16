'''Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.'''

idade = int(input("Digite a idade da pessoa: "))

if idade < 18:
    print("A pessoa é menor de idade.")
elif idade >= 18 and idade <= 65:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é maior de 65 anos. já ta muito velho")
