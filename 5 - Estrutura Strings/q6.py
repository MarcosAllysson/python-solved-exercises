"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""
from datetime import datetime


def data_por_extenso(dia, mes, ano):
    mes_usuario = ''
    meses = [
        '',
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro'
    ]

    for m in range(1, len(meses)):
        if m == mes:
            mes_usuario = meses[m]

    return f'Você nasceu em {dia} de {mes_usuario} de {ano}.'


try:
    ano_atual = datetime.now().year

    while True:
        data = input('Qual sua data de nascimento (Ex: 01/01/2000)? ').strip()
        dia = int(data[:2])
        mes = int(data[3:5])
        ano = int(data[6:10])

        if (1 <= dia <= 31) and (1 <= mes <= 12) and (1000 <= ano < ano_atual):
            print(data_por_extenso(dia, mes, ano))
            break
        print('Data inválida!')

except Exception as error:
    print(error)
