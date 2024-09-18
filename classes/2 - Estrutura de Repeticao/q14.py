"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.
"""


def calcula_quantidade(numeros):
    lista = [[], []]

    for numero in numeros:
        if numero % 2 == 0:
            lista[0].append(numero)
        else:
            lista[1].append(numero)

    return f'Há {len(lista[0])} números pares, e são eles: {lista[0]}' \
           f'\nE tem {len(lista[1])} números ímpares, e são eles: {lista[1]}'


while True:
    try:
        lista_num = list()
        for numero in range(5):
            lista_num.append(int(input(f'Informe: {numero+1}° valor: ')))

    except Exception as error:
        print(error)

    else:
        print(calcula_quantidade(lista_num))
        break
