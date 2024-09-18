"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
(0 °C × 9/5) + 32 = 32 °F)
"""

while True:
    try:
        cel = float(input('Converção de celcius: '))
        fah = (cel * 9 / 5) + 32
    except Exception as error:
        print(f'Ops, {error}')
    else:
        print(f'{cel}° para fahrenheit: {fah:.2f}°')
        break
