"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

from functools import reduce


def com_reduce(num1=0, num2=0):
    """
    Função que recebe 2 números e retorna o maior
    Usando função internet reduce(), juntamente com função lambda.
    No qual ele recebe 2 parâmetros, retornando A se A > B, senão, retorna B.
    """
    lista = [num1, num2]
    try:
        print(f'Maior é: {reduce(lambda a, b: a if a > b else b, lista)}')
    except Exception as error:
        print(f'Error: {error}')


def estrutura_condicional(num1=0, num2=0):
    """
    Função que recebe 2 números e retorna o maior com estrutura condicional simples
    Caso nenhum inteiro ou real seja informado, o mesmo é tratado com try-except
    """
    try:
        if num1 > num2:
            print(f'{num1} é \033[32mmaior\033[m que {num2}.')
        elif num2 > num1:
            print(f'{num2} é \033[32mmaior\033[m que {num1}.')
        else:
            print(f'{num1} é \033[32migual\033[m a {num2}.')
    except Exception as error:
        print(f'Não foi possível verificar... \n{error}')


def com_max(num1=0, num2=0):
    """
    Função que retorna o maior valor informado usando o max()
    """
    try:
        print(f'O maior é: {max(num1, num2)}')
    except Exception as error:
        print(f'Erro: {error}')


# Programa principal:
#com_reduce(3, 2)
#estrutura_condicional(2, 4)
#com_max(3, 10)
