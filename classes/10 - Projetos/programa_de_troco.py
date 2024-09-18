"""
Programa de troco - O usuário insere um custo e depois a quantia de dinheiro dada. O programa calcular o troco
(em reais e centavos).
"""


def programa_de_troco(custo: float, quantia: float) -> None:
    try:
        if 0 <= quantia >= custo >= 0:
            print(f'Custo R$: {custo:.2f}, quantia recebida R$: {quantia:.2f}'
                  f'\nTroco: R$ {quantia - custo:.2f}')
        else:
            print(f'Não foi possível realizar a operação! Quantia insuficiente. Faltam R$: {custo - quantia:.2f}, '
                  f'para completar a compra. ')

    except Exception as error:
        print(error)


programa_de_troco(120, 150)
