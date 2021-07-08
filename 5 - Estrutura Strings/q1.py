"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""


def strings(str_one, str_two):
    size_str_one = len(str_one)
    size_str_two = len(str_two)

    if size_str_one != size_str_two:
        message_siz = 'As duas strings são de tamanhos diferentes.'
    else:
        message_siz = 'As duas strings são de tamanhos iguais.'

    if str_one != str_two:
        message_str = 'As duas strings possuem conteúdo diferente.'
    else:
        message_str = 'As duas strings possuem conteúdo iguais.'

    return f'\n Tamanho de {str_one}: {size_str_one} caracteres' \
           f'\n Tamanho de {str_two}: {size_str_two} caracteres' \
           f'\n {message_siz}' \
           f'\n {message_str}'


try:
    str_one = str(input('String 1: '))
    str_two = str(input('String 2: '))
    print(strings(str_one, str_two))

except:
    print('Erro, tente novamente...')
