"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
from time import sleep

try:
    vetor_um = list()
    vetor_dois = list()
    vetor_tres = list()

    print('\n \033[36mLendo valores do vetor 1: \033[m')
    for num in range(10):
        vetor_um.append(int(input(f'Valor {num+1}: ')))

    print('\n \033[36mLendo valores do vetor 2: \033[m')
    for num in range(10):
        vetor_dois.append(int(input(f'Valor {num+1}: ')))

    print('\nOrganizando e apresentando vetores gerados...')
    sleep(1)
    print(vetor_um)
    print(vetor_dois)

    for num in range(10):
        vetor_tres.append(vetor_um[num])
        vetor_tres.append(vetor_dois[num])

    print('\nIntercalando valores...')
    sleep(2)
    print(f'{vetor_tres}')

except Exception as erro:
    print(erro)
