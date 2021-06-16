"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A) o produto do dobro do primeiro com metade do segundo .
B) a soma do triplo do primeiro com o terceiro.
C) o terceiro elevado ao cubo.
"""

while True:
    try:
        number_one = int(input('Digite um número inteiro: '))
        number_two = int(input('Digite o 2° número inteiro: '))
        number_thr = float(input('Agora informe um número real: '))

        problem_one = (number_one * 2) * (number_two / 2)
        problem_two = number_one * 3 + number_thr
        problem_thr = number_thr**3

    except Exception as error:
        print(f'Não consegui continuar o programa: {error.__class__}, descrição: {error}')
    else:
        print(f'\033[36m1° número é: {number_one}, 2° número é o {number_two} e o 3° número é o {number_thr}\033[m.')
        print(f' - O produto do dobro do primeiro com metade do segundo vale: {problem_one}.')
        print(f' - A soma do triplo do primeiro com o terceiro vale: {problem_two}.')
        print(f' - O terceiro elevado ao cubo vale: {problem_thr}.')
        break
