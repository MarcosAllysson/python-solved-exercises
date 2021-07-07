"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
from time import sleep

try:
    vetor_um = list()
    vetor_dois = list()
    vetor_tres = list()
    vetor_quatro = list()

    print('\n \033[36mLendo valores do vetor 1: \033[m')
    for num in range(10):
        vetor_um.append(int(input(f'Valor {num+1}: ')))

    print('\n \033[36mLendo valores do vetor 2: \033[m')
    for num in range(10):
        vetor_dois.append(int(input(f'Valor {num+1}: ')))

    print('\n \033[36mLendo valores do vetor 3: \033[m')
    for num in range(10):
        vetor_tres.append(int(input(f'Valor {num + 1}: ')))

    print('\nOrganizando e apresentando vetores gerados...')
    sleep(1)
    print(vetor_um)
    print(vetor_dois)
    print(vetor_tres)

    for num in range(10):
        vetor_quatro.append(vetor_um[num])
        vetor_quatro.append(vetor_dois[num])
        vetor_quatro.append(vetor_tres[num])

    print('\nIntercalando valores...')
    sleep(2)
    print(f'{vetor_quatro}')

except Exception as erro:
    print(erro)
