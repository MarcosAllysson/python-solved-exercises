"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""


def numero(* num):
    lista = num[0]
    return f'\nMenor: {min(lista)}' \
           f'\nMaior: {max(lista)}' \
           f'\nSoma:  {sum(lista)}'


while True:
    try:
        lista_num = []
        while True:
            num = int(input('Informe um número ou "999" para parar: '))
            if num != 999:
                lista_num.append(num)
            else:
                break

    except Exception as e:
        print(e)

    else:
        print(numero(lista_num))
        break
