"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

while True:
    try:
        base = float(input('Informe a base do quadrado (b): '))
        altura = float(input('Agora me diga o altura (h): '))
        area_quadrado = base * altura
        dobro_da_area = area_quadrado * 2
    except Exception as error:
        print(f'Arruma esse erro: {error.__class__}, descrição: {error} ')
    else:
        print(f'Área do quadrado é {area_quadrado}m, e o dobro da área vale {dobro_da_area}m.')
        break
