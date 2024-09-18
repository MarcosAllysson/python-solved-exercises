while True:
    """
    Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
    Dica: utilize uma função de arredondamento.
    """
    try:
        numero = float(input('Informe um número: '))

        if numero == round(numero):
            print(f'{numero} é inteiro.')
            break  # saindo do loop
        else:
            print(f'{numero} é decimal.')
            break

    except:
        print('Houve um error, tente novamente! ')
