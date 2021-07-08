"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def print_line(num):
    for n in range(1, num + 1):
        print(f' {n} ', end='')
    print()


def print_sequence(num):
    for num in range(num + 1):
        print_line(num)


try:
    value = int(input('Digite número inteiro: '))
    if value >= 1:
        print_sequence(value)
    else:
        print('Somente número inteiro maior que 1.')

except:
    print('Erro, tente novamente...')
