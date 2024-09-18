def validador(num=0):
    """
    Funçõa que informa se o número é positivo ou negativo.
    """
    return lambda x: num >= 0


# Programa principal
while True:
    try:
        numero = float(input('Informe um valor: '))

    except Exception as error:
        print(f'Error: {error}.\nTente novamente.')

    else:
        if validador(numero):
            print(f'{numero} é positivo.')
        else:
            print(f'{numero} é negativo.')

        # saindo do loop
        break
