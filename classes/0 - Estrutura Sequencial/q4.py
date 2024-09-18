"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

while True:
    try:
        notas = list()
        for i in range(0, 4):
            nota = float(input(f'Digite {i+1}° nota: '))
            notas.append(nota)

        media = sum(notas) / len(notas)
    except Exception as error:
        print(f'Não consegui calcular a média, exceção: \033[31m{error.__class__}\033[m, descrição: \033[31m{error}\033[m ')
    else:
        print(f'Média das notas é: {media:.2f}')
        break
