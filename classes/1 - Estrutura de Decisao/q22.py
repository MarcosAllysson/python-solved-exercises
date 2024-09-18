def par_ou_impar(numero):
    """
    Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
    Dica: utilize o operador módulo (resto da divisão).
    """
    resultado = lambda x: x % 2 == 0
    return resultado(numero)


while True:
    try:
        numero = int(input('Informe um número: '))

    except Exception as error:
        print(f'Error: {error.__class__}, descrição: {error}.')

    else:
        if par_ou_impar(numero):
            print(f'{numero} é par.')
        else:
            print(f'{numero} é ímpar.')
        break
