"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""


def triangulo(angulo1, angulo2, angulo3):
    if (angulo1 + angulo2) > angulo3 and (angulo2 + angulo3) > angulo1 and (angulo3 + angulo1) > angulo2:
        msg = '\nOs lados informados podem sim formar um triângulo!'

        if angulo1 == angulo2 == angulo3:
            return f'{msg}\nTriângulo Equilátero: três lados iguais.'

        elif angulo1 != angulo2 != angulo3:
            return f'{msg}\nTriângulo Escaleno: três lados diferentes.'

        else:
            return f'{msg}\nTriângulo Isósceles: quaisquer dois lados iguais.'

    else:
        return '\nNão é possível formar um triângulo.'


#  programa principal
while True:
    try:
        angulo1 = int(input('Informe 1° lado: '))
        angulo2 = int(input('Informe 2° lado: '))
        angulo3 = int(input('Informe 3° lado: '))

        print(f'Lados recebidos: {angulo1, angulo2, angulo3}.')

    except Exception as error:
        print(f'Error: {error.__class__}, {error}.')

    else:
        print(triangulo(angulo1, angulo2, angulo3))
        break
