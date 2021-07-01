from time import sleep
"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

while True:
    try:
        vetores = []
        for num in range(1, 6):
            vetores.append(int(input(f'Informe valor inteiro {num}: ')))

    except Exception as error:
        print(f'Erro: {error.__class__}, descrição: {error}.')

    else:
        print('\nLendo vetores recebidos: ')
        sleep(2)

        for num in vetores:
            print(f'\033[33m{num}\033[m', end=' - ')

        # saindo o loop
        break
