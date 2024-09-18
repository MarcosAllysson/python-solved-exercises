"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""


def crescimento_populacional(pais_1, pais_2):
    pais_1_p = pais_1['populacao']
    pais_1_t = pais_1['taxa_crescimento']

    pais_2_p = pais_2['populacao']
    pais_2_t = pais_2['taxa_crescimento']

    anos_necessarios = 0
    if pais_1_p <= pais_2_p:
        while pais_1_p <= pais_2_p:
            #  Enquanto país A menor ou igual ao país B, aumento x% de cada país, somando 1 aos anos.
            pais_1_p += pais_1_p * (pais_1_t / 100)
            pais_2_p += pais_2_p * (pais_2_t / 100)
            anos_necessarios += 1

    elif pais_2_p <= pais_1_p:
        while pais_2_p <= pais_1_p:
            pais_1_p += pais_1_p * (pais_1_t / 100)
            pais_2_p += pais_2_p * (pais_2_t / 100)
            anos_necessarios += 1

    return f'\n \033[36mPara que o país ultrapasse ou iguale ao outro país, são necessários {anos_necessarios} anos.\033[m'


while True:
    pais_a = {}
    pais_b = {}
    try:
        pais_a['populacao'] = int(input('Informe a população do país A: '))
        pais_a['taxa_crescimento'] = float(input('Taxa de crescimento: '))

        pais_b['populacao'] = int(input('Informe a população do país B: '))
        pais_b['taxa_crescimento'] = float(input('Taxa de crescimento: '))

    except Exception as error:
        print(f'Erro: {error}')

    else:
        print(crescimento_populacional(pais_a, pais_b))
        break
