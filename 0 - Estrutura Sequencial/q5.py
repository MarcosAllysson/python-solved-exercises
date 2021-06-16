"""
Faça um Programa que converta metros para centímetros.
"""

while True:
    try:
        metro = float(input('Converta de \033[36mmetros\033[m para \033[35mcentímentros\033[m: '))
        conversão = metro * 100
    except Exception as error:
        print(f' Não consegui converter, erro: {error.__class__}, descrição: {error}. ')
    else:
        print(f' Convertendo {metro:.0f}m pra centímentro: {conversão:.2f}cm.')
        break
