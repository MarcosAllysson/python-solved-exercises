"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:
A) Para homens: (72.7*h) - 58
B) Para mulheres: (62.1*h) - 44.7
"""

while True:
    try:
        # altura
        altura = float(input('Qual seu altura? '))

        # sexo com validação
        while True:
            sexo = str(input('Qual seu sexo? (H/M)? ')).strip().upper()[0]
            if sexo in 'HM':
                break
            print('Digite somente H para Homem ou M para Mulher!')

        # calculando peso ideal:
        if sexo == 'H':
            peso_ideal = (72.7 * altura) - 58
        else:
            peso_ideal = (62.1 * altura) - 44.7
    
    except Exception as error:
        print(f'Não consegui calcular seu peso ideal - Problema {error.__class__}, descrição: {error}.')

    else:
        print(f'Sua altura: {altura}m, seu sexo: {sexo} e o seu peso ideal é {peso_ideal:.2f}kg.')
        break
