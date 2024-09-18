"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""


def calcula_preco(quantidade_kg_morango, quantidade_kg_maca):
    #  calculando preço de cada fruta
    if quantidade_kg_morango <= 5:
        preco_morango = quantidade_kg_morango * 2.50

    else:
        preco_morango = quantidade_kg_morango * 2.20

    if quantidade_kg_maca <= 5:
        preco_maca = quantidade_kg_maca * 1.80

    else:
        preco_maca = quantidade_kg_maca * 1.50

    #  calculando preço total
    preco_total = preco_maca + preco_morango
    kg_total = quantidade_kg_maca + quantidade_kg_morango

    if kg_total > 8 or preco_total > 25:
        preco_total -= (preco_total * 0.1)

    return f'\n\033[4;36mTABELA:\033[m' \
           f'\nMorango: {quantidade_kg_morango:.1f}kg, preço: R$ {preco_morango:.2f}' \
           f'\nMaça: {quantidade_kg_maca:.1f}kg, preço: R$ {preco_maca:.2f}' \
           f'\n\033[32mValor final:\033[m R$ {preco_total:.2f}'


while True:
    try:
        while True:
            quantidade_kg_morango = float(input('Quantos kg de morango? '))
            quantidade_kg_maca = float(input('Quantos kg de maça? '))

            if quantidade_kg_maca >= 0 and quantidade_kg_morango >= 0:
                break
            print('Quantidade inválida.')

    except Exception as error:
        print(f'\033[31mErro: {error.__class__}, descrição: {error}\nTente novamente!\033[m')

    else:
        print(calcula_preco(quantidade_kg_morango, quantidade_kg_maca))
        break
