'''Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.'''

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    dia_semana = "Domingo"
elif numero == 2:
    dia_semana = "Segunda-feira"
elif numero == 3:
    dia_semana = "Terça-feira"
elif numero == 4:
    dia_semana = "Quarta-feira"
elif numero == 5:
    dia_semana = "Quinta-feira"
elif numero == 6:
    dia_semana = "Sexta-feira"
elif numero == 7:
    dia_semana = "Sábado"
else:
    dia_semana = "Número inválido"

print(dia_semana)