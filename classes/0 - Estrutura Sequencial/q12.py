"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

while True:
    try:
        altura = float(input('Qual sua altura? '))
        peso = float(input('E qual seu peso? '))
        peso_ideal = (72.7 * altura) - 58

        if peso < peso_ideal:
            print(f'Você está {peso_ideal - peso:.2f}kg \033[31mabaixo\033[m do seu peso ideal.')
        else:
            print(f'Você está {peso - peso_ideal:.2f}kg \033[31macima\033[m do seu peso ideal.')

    except Exception as error:
        print(f'Não consegui calcular peso ideal: {error.__class__}, descrição: {error}')
    else:
        print(f'Seu peso ideal é: {peso_ideal:.2f}kg')
        break
