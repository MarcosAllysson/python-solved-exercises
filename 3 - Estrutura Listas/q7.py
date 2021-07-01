from functools import reduce
"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""


def vetor_numero(vetor):
    soma = reduce((lambda a, b: a + b), vetor)
    mult = reduce((lambda a, b: a * b), vetor)

    return f'\nSoma: {soma}' \
           f'\nMult: {mult}' \
           f'\nNúmeros: {vetor}'


try:
    vetor = list()
    for num in range(5):
        vetor.append(int(input(f'Valor {num+1}: ')))

    print(vetor_numero(vetor))

except Exception as error:
    print(error)
