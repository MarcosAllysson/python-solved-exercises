from functools import reduce


def produto_mais_barato(* valores):
    """
    Programa que pergunta o preço de três produtos e informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato.
    """
    precos = list()
    for valor in valores[0]:
        precos.append(valor)

    return reduce(lambda valor_a, valor_b: valor_a if (valor_a < valor_b) else valor_b, precos)


while True:
    try:
        precos = list()
        for i in range(3):
            precos.append(float(input(f'Preço do {i+1}° produto: R$ ')))

        print(f'Ok, valores informados foram: {precos}.')

    except Exception as error:
        print(f'Houve um erro: {error}. \nTente novamente.')

    else:
        print(f'Compre o produto mais barato que custa R$ {produto_mais_barato(precos)}.')
        break
