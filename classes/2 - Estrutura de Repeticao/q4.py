"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
"""


def crescimento_populacional(pais_1, pais_2):
    pais_1_p = pais_1['populacao']
    pais_1_t = pais_1['taxa_crescimento']

    pais_2_p = pais_2['populacao']
    pais_2_t = pais_2['taxa_crescimento']

    anos_necessarios = 0
    while pais_1_p <= pais_2_p:
        #  Enquanto país A menor ou igual ao país B, aumento 3% e 1.5% de cada país, somando 1 aos anos.
        pais_1_p += (pais_1_p * 0.03)
        pais_2_p += (pais_2_p * 0.015)
        anos_necessarios += 1

    return f'\n \033[32mPaís 1:\033[m população de {pais_1_p} habitantes, que cresce {pais_1_t}%' \
           f'\n \033[32mPais 2:\033[m população de {pais_2_p} habitantes, que cresce {pais_2_t}%' \
           f'\n \033[35mPara que o país A ultrapasse ou iguale o país B, são necessários {anos_necessarios} anos.\033[m'


pais_a = {'populacao': 80000, 'taxa_crescimento': 3}
pais_b = {'populacao': 200000, 'taxa_crescimento': 1.5}

print(crescimento_populacional(pais_a, pais_b))
