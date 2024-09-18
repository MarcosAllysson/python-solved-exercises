"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""

print(' \033[36m1° opção: \033[m')
lista_1 = [i for i in range(1, 51)]
impares_1 = list(filter(lambda x: x % 2 != 0, lista_1))
print(impares_1)


print('\n \033[36m2° opção: \033[m')
lista_2 = [i for i in range(1, 51, 2)]
print(lista_2)


print('\n \033[36m3° opção: \033[m')
impares_3 = list(filter(lambda x: x % 2 != 0, [i for i in range(1, 51)]))
print(impares_3)


print('\n \033[36m4° opção: \033[m')
impares_4 = [i for i in range(1, 51)]
for num in impares_4:
    if num % 2 != 0:
        print(num, end=', ')
