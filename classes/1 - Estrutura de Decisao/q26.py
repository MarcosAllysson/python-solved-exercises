"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
    - até 20 litros, desconto de 3% por litro
    - acima de 20 litros, desconto de 5% por litro
Gasolina:
    - até 20 litros, desconto de 4% por litro
    - acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""


def posto_de_gasolina(litros, tipo_de_combustível):
    if tipo_de_combustível == 'A':
        alcool_sem_desconto = litros * 1.90

        if litros <= 20:
            calculo_valor_pago = alcool_sem_desconto - (alcool_sem_desconto * 0.03)
        else:
            calculo_valor_pago = alcool_sem_desconto - (alcool_sem_desconto * 0.05)

    else:
        gasolina_sem_desconto = litros * 2.50

        if litros <= 20:
            calculo_valor_pago = gasolina_sem_desconto - (gasolina_sem_desconto * 0.04)
        else:
            calculo_valor_pago = gasolina_sem_desconto - (gasolina_sem_desconto * 0.06)

    return f'\n\033[4;36mCÁLCULO FINAL A SER PAGO:\033[m ' \
           f'\nLitros: {litros}l' \
           f'\nCombustível: {tipo_de_combustível}' \
           f'\nValor a ser pago: R$ {calculo_valor_pago:.2f}'


while True:
    try:
        while True:
            litros = float(input('Informe quantos litros foram vendidos: '))
            if litros >= 1:
                break
            print(f'Informe no mínimo 1 litro.')

        while True:
            tipo_de_combustível = str(input('Tipo de combustível? \nA-álcool\nG-gasolina \nOpção: ')).strip().upper()[0]
            if tipo_de_combustível in 'AG':
                break
            print('Opção inválida. Escolha álcool ou gasolina.')

    except:
        print('Erro, tente novamente...')

    else:
        print(posto_de_gasolina(litros, tipo_de_combustível))
        break
