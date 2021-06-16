def calcula_potencia(base, expoente):
    """
    Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
    Não utilize a função de potência da linguagem.
    """
    numero_elevado = 1

    for i in range(expoente):
        numero_elevado *= base

    return f'\n{base} elevado a {expoente} = {numero_elevado}.'


while True:
    try:
        while True:
            base = int(input('Informe a base: '))
            expoente = int(input('Expoente: '))
            if base >= 0 and expoente >= 0:
                break
            print(f'\033[mInsira somente valores positivos!\033[m')

        print(calcula_potencia(base, expoente))
        break

    except Exception as error:
        print(error)
