from datetime import date


def calculo_ano_bissexto(ano):
    """
    Programa que pede um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
    Fórmula: Anos divisíveis por 4 e NÃO divisível por 100 ou divisível por 400 são considerados bissextos.
    """
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return f'{ano} é bissexto.'
    else:
        return f'{ano} não é bissexto.'


while True:
    try:
        while True:
            ano = str(input('Informe um ano para verificar se é bissexto: '))

            if len(ano) == 4 and ano.isdigit():
                break
            print('Ano inválido! Digite 4 dígitos no formato XXXX.')

    except Exception as error:
        print(f'Error: {error}.')

    else:
        print(calculo_ano_bissexto(int(ano)))
        break
