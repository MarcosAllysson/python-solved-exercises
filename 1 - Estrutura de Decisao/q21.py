def caixa_eletronico(valor):
    """
    Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
    informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
    O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
    existentes na máquina.
    """
    notas100 = valor // 100
    notas50 = (valor % 100) // 50
    notas10 = (valor % 50) // 10
    notas5 = (valor % 10) // 5
    notas1 = (valor % 5) // 1

    return f'Para sacar o valor de R$ {valor:.2f}, o programa fornece de {notas100} notas de 100, {notas50} notas de 50,' \
           f' {notas10} notas de 10, {notas5} notas de 5 e {notas1} notas de 1.'


while True:
    try:
        while True:
            valor = int(input('Informe o valor do saque: R$ '))
            if 10 <= valor <= 600:
                break
            print('Valor mínimo é de R$ 10,00 e no máximo R$ 600,00.')

    except Exception as error:
        print(f'Error: {error.__class__}, descrição: {error}.')

    else:
        print(caixa_eletronico(valor))
        break
