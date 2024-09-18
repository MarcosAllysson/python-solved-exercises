"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def positivo_ou_negativo(arg: int) -> str:
    if arg > 0:
        return 'P'
    else:
        return 'N'


try:
    num = int(input('Argumento: '))
    print(positivo_ou_negativo(num))

except Exception as error:
    print(error)
