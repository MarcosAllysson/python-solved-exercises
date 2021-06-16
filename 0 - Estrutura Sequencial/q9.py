"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

while True:
    try:
        fah = float(input('Converta de Fahrenheit: '))
        cel = 5 * ((fah - 32) / 9)
    except Exception as error:
        print(f'Ops, {error.__class__}, descrição: {error}. ')
    else:
        print(f'{fah}° Fahrenheit para celcius: {cel:.2f}° ')
        break
