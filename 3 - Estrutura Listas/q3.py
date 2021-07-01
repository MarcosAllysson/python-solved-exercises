"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""


def media_notas(* notas):
    media = sum(notas[0]) / len(notas[0])

    return f'\n \033[1;31mA média das notas: {notas[0]} é: {media:.1f} \033[m'


try:
    notas = list()
    for num in range(4):
        while True:
            nota = float(input(f'{num+1}° nota: '))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print('Nota somente entre 0 e 10 (incluídos.)')

    print(media_notas(notas))

except:
    print(f'Algum erro aconteceu, tente novamente...')
