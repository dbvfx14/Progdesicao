'''Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente'''

a = int(input("Informe o valor para a: "))
b = int(input("Informe o valor para b:"))
c = int(input("Informe o valor para c: "))

# 1 - a tem que ser menor que b
if (a > b):
    aux = a
    a = b
    b = aux
# garantido ate aqui entre a e b, o menor esta em a

# 2- a tem que ser menor que c
if (a > c):
    aux = a
    a = c
    c = aux
# garanrindo até aqui que a é o menor dos 3
# agora é necessario garantir que b seja menor que c
if (b > c):
    aux = b
    b = c
    c = aux
# garantindo ate aqui entre b e c, o b é menor, ou seja, o c é maior de todos
print(f"Ordem crescente: {a}, {b} e {c}")