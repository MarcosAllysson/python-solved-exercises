"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
"""


def supermercado_tabajara(tipo_de_carne, quantidade_de_carne):
    """
    Função que calcula o preço a ser pago pelo cliente.
    """
    tabela_preco_carnes = {
        'File_Duplo': [4.90, 5.80],
        'Alcatra': [5.90, 6.80],
        'Picanha': [6.90, 7.80]
    }

    if tipo_de_carne == 'F':
        if quantidade_de_carne <= 5:
            preco_carne = quantidade_de_carne * tabela_preco_carnes['File_Duplo'][0]

        else:
            preco_carne = quantidade_de_carne * tabela_preco_carnes['File_Duplo'][1]

    elif tipo_de_carne == 'A':
        if quantidade_de_carne <= 5:
            preco_carne = quantidade_de_carne * tabela_preco_carnes['Alcatra'][0]

        else:
            preco_carne = quantidade_de_carne * tabela_preco_carnes['Alcatra'][1]

    elif tipo_de_carne == 'P':
        if quantidade_de_carne <= 5:
            preco_carne = quantidade_de_carne * tabela_preco_carnes['Picanha'][0]
        else:
            preco_carne = quantidade_de_carne * tabela_preco_carnes['Picanha'][1]

    tipo_de_pagamento = 'Dinheiro, Cartão de Crédito ou Tabajara (5% desconto)'
    cartao_tabajara_desconto = preco_carne - (preco_carne * 0.05)

    return cupom_fiscal(tipo_de_carne, quantidade_de_carne, preco_carne, tipo_de_pagamento, cartao_tabajara_desconto)


def cupom_fiscal(tipo_de_carne, quantidade_de_carne, preco_carne, tipo_de_pagamento, cartao_tabajara_desconto):
    """
    Função para printar mensagem do cupom fiscal
    """
    print()
    print('-' * 34)
    print('\033[33mMERCADO TABAJARA - CUPOM FISCAL:\033[m')
    print('-' * 34)
    print(f'\033[36mTipo de carne:\033[m       {tipo_de_carne}')
    print(f'\033[36mQuantidade:\033[m          {quantidade_de_carne}kg')
    print(f'\033[36mPreço total:\033[m         R$ {preco_carne:.2f}')
    print(f'\033[36mPagamento:\033[m           {tipo_de_pagamento}')
    print(f'\033[36mCom cartão tabajara:\033[m R$ {cartao_tabajara_desconto:.2f}')


#  programa principal
while True:
    try:
        while True:
            tipo_de_carne = str(input('Qual carne você quer?'
                                      '\n - File Duplo'
                                      '\n - Alcatra'
                                      '\n - Picanha'
                                      '\nSua escolha: ')).strip().upper()[0]
            if tipo_de_carne in 'FAP':
                break
            print('\n \033[1;31mEscolha inválida... Se preferir, digite apenas a 1° letra da carne que você quer\033[m')

        while True:
            quantidade_de_carne = float(input('Você quer quantos kilos? '))
            if quantidade_de_carne > 0:
                break
            print(f'\033[1;31mErro: escolha pelo menos 1 kg de carne!\033[m')

    except:
        print('Houve um erro, tente novamente...')

    else:
        supermercado_tabajara(tipo_de_carne, quantidade_de_carne)
        break
