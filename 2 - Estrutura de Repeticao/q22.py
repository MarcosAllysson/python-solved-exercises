def eh_primo(numero):
    """
    Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
    divisível.
    """
    cont_div = 0
    divisiveis = list()

    for i in range(1, numero+1):
        if numero % i == 0:
            cont_div += 1
            divisiveis.append(i)

    if cont_div == 2:
        return f'{numero} é primo'
    else:
        return f'{numero} não é primo, pois e divisível por: {divisiveis}'


while True:
    try:
        numero = int(input('Informe um número inteiro: '))

    except Exception as erro:
        print(f'{erro}')

    else:
        print(eh_primo(numero))

        break

