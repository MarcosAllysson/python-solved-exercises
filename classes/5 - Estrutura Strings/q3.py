"""
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
"""


def name(str):
    for letter in str:
        print(letter)


try:
    string = str(input('Qual seu nome? ')).strip()
    name(string)

except Exception as error:
    print(error)
