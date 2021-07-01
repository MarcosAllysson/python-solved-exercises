"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
"""


try:
    vetor = [[], []]

    for val in range(20):
        numero = int(input(f'Informe o {val+1}° número: '))
        if numero % 2 == 0:
            vetor[0].append(numero)
        else:
            vetor[1].append(numero)

except Exception as error:
    print(error)

else:
    print(f'\nTodos os vetores: {vetor}'
          f'\nNúmeros pares: {vetor[0]}'
          f'\nÍmpares: {vetor[1]}')
