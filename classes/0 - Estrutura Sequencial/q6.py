#
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
# AŔEA = pi * raio**

while True:
    try:
        raio = 0
        raio = float(input('Digite o raio: '))
        area = 3.14 * raio**2
    except Exception as error:
        print(f'Não consegui calcular o raio de {raio} por que, {error.__class__}, descrição: {error}. ')
    else:
        print(f'Área de {raio} é {area}m. ')
        break
