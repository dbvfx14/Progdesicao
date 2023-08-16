'''Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.'''

ano = int(input("digite o ano de nascimento:"))
ano_atual = int(input("digite o ano atual:"))


if ano > ano_atual:
    print("Data invalida")

else:
    idade = ano_atual - ano
    print(f"A sua idade é {idade} anos")