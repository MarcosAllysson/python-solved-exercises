"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome
do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário
pode digitar letras maiúsculas ou minúsculas.
"""


def behind_string(str):
    return f'{str[::-1].upper()}'


try:
    word = str(input('Você pode digitar letras maiúsculas ou minúsculas!\nPalavra: '))
    print(behind_string(word))

except:
    print('Erro, tente novamente...')
