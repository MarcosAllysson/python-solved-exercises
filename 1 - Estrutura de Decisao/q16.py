def valida_data(data):
    """
    Programa que pede uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
    """
    data_valida = False
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses_30_dias = [4, 6, 9, 11]

    #  validando comprimento do dia, mês e ano.
    try:
        if len(data[:2]) == 1 or len(data[:2]) == 2 and len(data[3:5]) == 1 or len(data[3:5]) == 2 and len(data[6:]) == 4:
            dia = int(data[:2])
            mes = int(data[3:5])
            ano = int(data[6:])

        else:
            return f'\nData: {data}, \033[1;31minválida!\033[m'
            exit()

    except Exception as error:
        return f'\nError: {error}.\nData inválida! Tente novamente'
        exit()

    #  meses que têm 31 dias:
    if mes in meses_31_dias and 1 <= dia <= 31:
        data_valida = True

    elif mes in meses_30_dias and 1 <= dia <= 30:
        data_valida = True

    #  fevereiro e ano bissexto:
    elif mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if 1 <= dia <= 29:
                data_valida = True

        elif 1 <= dia <= 28:
            data_valida = True

    if data_valida:
        return f'\nA data informada, dia: {dia}, mes: {mes}, ano: {ano}\nÉ uma data válida!'

    else:
        return f'\nData inválida.'


while True:
    try:
        data = str(input('Informe uma data no formato dd/mm/aaaa: '))
        print(f'\033[1;32mAnalisando: {data}\033[m')

    except Exception as error:
        print(f'\nError: {error}.')

    else:
        print(valida_data(data))
        break
