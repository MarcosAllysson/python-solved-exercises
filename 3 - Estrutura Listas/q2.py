"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
from random import randint

try:
    vetor = list()
    # outra maneira gerando valores aleatórios.
    #for i in range(10):
    #    vetor.append(randint(0, 10))

    for i in range(10):
        vetor.append(float(input(f'Informe {i+1}° número real: ')))

    print(f'Original: {vetor}')
    print(f'Inverso: {vetor[::-1]}')

except Exception as e:
    print(f'Error: {e}')
