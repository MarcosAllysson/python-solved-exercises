from functools import reduce
# from random import randint
"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do 
vetor.
"""

try:
    vetores_inteiros = []
    for i in range(10):
        vetores_inteiros.append(int(input(f'{i+1}° vetor: ')))
        # vetores_inteiros.append(int(randint(1, 100)))

    vetor_ao_quadrado = list(map(lambda x: x ** 2, vetores_inteiros))
    soma_vetor_ao_quadrado = reduce(lambda a, b: a + b, vetor_ao_quadrado)
    print(f'Soma dos quadrados: {soma_vetor_ao_quadrado}')

except Exception as erro:
    print(erro)
