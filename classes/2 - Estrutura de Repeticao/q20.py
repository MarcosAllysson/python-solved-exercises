from math import factorial
"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
"""


def fatorial(num):
    print(f'\033[32m \bFatorial de {num} = \033[m {factorial(num)}.')


while True:
    try:
        while True:
            num = int(input('Informe um número inteiro (entre 0 e 16) para calcular o fatorial OU (99) para parar: '))
            if 0 <= num <= 16:
                fatorial(num)
            elif num == 99:
                break

    except Exception as error:
        print(f'{error}')

    else:
        break
