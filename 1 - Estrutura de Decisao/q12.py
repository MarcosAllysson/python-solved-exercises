def semana(dia):
    """
    Programa que lê um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
    se digitar outro valor deve aparecer valor inválido.
    """
    if dia == 1:
        return f'Dia {dia}: domingo!'
    elif dia == 2:
        return f'Dia {dia}: segunda!'
    elif dia == 3:
        return f'Dia {dia}: terça!'
    elif dia == 4:
        return f'Dia {dia}: quarta!'
    elif dia == 5:
        return f'Dia {dia}: quinta!'
    elif dia == 6:
        return f'Dia {dia}: sexta!'
    else:
        return f'Dia {dia}: sábado!'


while True:
    try:
        while True:
            dia_da_semana = int(input('Informe um número: '))
            if 1 <= dia_da_semana <= 7:
                break
            print('Número inválido, vá somente de 1 a 7.')

    except Exception as error:
        print(f'Erro {error.__class__}: {error}.\nTente novamente!')

    else:
        print(semana(dia_da_semana))
        break
