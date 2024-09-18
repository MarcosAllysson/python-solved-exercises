"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def sum_numbers(*args) -> list:
    return f'Soma: {sum(args[0])}'


try:
    numbers = []
    for i in range(3):
        numbers.append(int(input(f'Argumento {i+1}: ')))

    print(sum_numbers(numbers))
except:
    print('Erro, tente novamente...')
