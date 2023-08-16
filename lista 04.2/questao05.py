'''Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.'''

estado = input("Digite a sigla de um estado brasileiro: ")

regiao_sudeste = ["SP", "RJ", "MG", "ES"]

if estado == "SP" or estado == "RJ" or estado == "MG" or estado == "ES":
    print("O estado inserido está na região Sudeste.")
else:
    print("O estado inserido não está na região Sudeste.")