def eh_primo(numero):
    """
    Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
    Um número primo é aquele que é divisível somente por ele mesmo e por 1.
    """
    cont_div = 0
    primo = False

    for i in range(1, numero+1):
        if numero % i == 0:
            cont_div += 1

    if cont_div == 2:
        primo = True

    return primo


while True:
    try:
        numero = int(input('Informe um número inteiro: '))

    except Exception as erro:
        print(f'{erro}')

    else:
        if eh_primo(numero):
            print(f'{numero} é primo.')
        else:
            print(f'{numero} não é primo.')

        break
