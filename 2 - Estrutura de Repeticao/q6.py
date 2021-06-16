"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro.
"""

print('\033[36m1° modo de exibição:\033[m ')
lista = [i for i in range(1, 21)]
for i in lista:
    print(i, end='')
    if i < 20:
        print(';')
    else:
        print('.')


print('\n \033[36m2° modo de exibição:\033[m ')
for i in lista:
    print(i, end='')
    if i < 20:
        print(', ', end='')
    else:
        print('.')
