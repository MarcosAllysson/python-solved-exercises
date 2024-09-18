"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""

try:
    num_user = int(input('Value: '))
    if 0 <= num_user:
        for num in range(1, num_user + 1):
            print(str(num) * num)
    else:
        print('Somente valor inteiro!')

except:
    print('Erro, tente novamente.')
