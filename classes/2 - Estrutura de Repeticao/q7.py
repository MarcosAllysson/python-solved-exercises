"""
Faça um programa que leia 5 números e informe o maior número.
"""


def mostra_maior_numero(* numeros):
    maior = cont = 0

    for numero in numeros[0]:
        if cont == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero

        cont += 1

    return f'\033[36mMaior: {maior}\033[m'


while True:
    try:
        lista_numeros = []
        for i in range(5):
            lista_numeros.append(int(input(f'Informe o {i+1}° número: ')))

    except Exception as error:
        print(f'Error: {error.__class__}, descrição: {error}.')

    else:
        print(mostra_maior_numero(lista_numeros))
        break
