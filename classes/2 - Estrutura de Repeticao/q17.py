from math import factorial
from time import sleep
"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""


def fatorial(num):
    print(f'\033[32mCalculando fatorial de {num}...\033[m')
    sleep(2)
    print(f'\033[32mCom função interna do python:\033[m {factorial(num)}')
    print(f'\033[32mCom laço:\033[m {num}! = ', end='')
    fat = 1

    for i in range(1, num):
        fat = num * (num - 1)

    print(fat)


while True:
    try:
        num = int(input('Informe um número inteiro para calcular o fatorial: '))

    except Exception as error:
        print(f'{error}')

    else:
        fatorial(num)
        break
