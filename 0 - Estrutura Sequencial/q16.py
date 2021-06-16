"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
de latas de tinta a serem compradas e o preço total.
"""

print('\033[34mLOJA DE TINTAS\033[m\n')

def lojaDeTinta():
    while True:
        try:
            tamanho_area_pintada = float(input('Qual tamanho em metros quadrados a ser pintada? '))
            litros_necessarios = tamanho_area_pintada / 3
            latas_necessarias = int(litros_necessarios / 18)
            if latas_necessarias < 1:
                latas_necessarias = 1
            valor_final = latas_necessarias * 80

        except Exception as error:
            print(f'Error: {error}.')

        else:
            print(f'Tamanho da área: {tamanho_area_pintada}m2'
                  f'\nCobertura de tinta: {litros_necessarios:.2f}lts'
                  f'\nNecessário: {latas_necessarias} latas de tinta'
                  f'\nValor final: R$ {valor_final:.2f}')
            break


# programa principal
lojaDeTinta()