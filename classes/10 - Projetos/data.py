from datetime import datetime, date, timedelta


def data(operation, dias=0):
    hoje = date.today()

    if operation == 'soma':
        op = hoje + timedelta(days=dias)
        print(f'Hoje é: {hoje}'
              f'\nDaqui {dias} dias, será dia: {op}')

        if hoje == op:
            print('Hoje é hoje!')
        if hoje > op:
            print('Futuro...')
        if hoje < op:
            print('Passado...')

    if operation == 'sub':
        op = hoje - timedelta(days=dias)
        print(f'Hoje é: {hoje}'
              f'\nHá {dias} dias atrás, foi dia: {op}')

        if hoje == op:
            print('Hoje é hoje!')
        if hoje > op:
            print('Futuro...')
        if hoje < op:
            print('Passado...')

    if operation == 'folga':
        op = hoje + timedelta(days=dias)
        print(f'Hoje é: {hoje}')

        if hoje <= op:
            print(f'Tudo certo com sua folga para o dia {op}, daqui {dias} dias.')
        else:
            print(f'Não tem como folgar no passado')


data('folga', 10)
# data('soma', 2)
# data('sub', 9)
