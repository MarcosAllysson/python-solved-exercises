"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""


def calcula_media(lista):
    return f'Soma: {sum(lista):.2f} \nMédia: {sum(lista) / len(lista):.2f}'

while True:
    try:
        lista = list()
        for i in range(5):
            lista.append(float(input(f'Informe o {i+1}° número: ')))

    except Exception as error:
        print(f'Erro: {error.__class__}, descrição: {error}.')

    else:
        print(calcula_media(lista))
        break
