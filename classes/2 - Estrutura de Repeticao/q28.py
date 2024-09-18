"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""


def total_investido(quantidade_cds, preco):
    return f'\nQuantidade de CDs: {quantidade_cds}' \
           f'\nTotal investido: R$ {sum(preco):.2f}' \
           f'\nValor médio: R$ {sum(preco) / quantidade_cds:.2f} por CD.'


try:
    preco = []
    quantidade_cds = int(input('Quantos CDs possui? '))

    for i in range(1, quantidade_cds+1):
        preco.append(float(input(f'Valor do CD {i}: R$ ')))

except Exception as e:
    print(e)

else:
    print(total_investido(quantidade_cds, preco))
