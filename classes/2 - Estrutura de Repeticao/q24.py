"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""


def calcula_media(* notas):
    nota = []
    for n in notas[0]:
        nota.append(n)

    return f'\n \033[36mMédia das notas:\033[m {sum(nota) / len(nota):.2f}'


while True:
    try:
        notas = []
        while True:
            valida_nota = float(input('Informe nota: '))
            if 0 <= valida_nota <= 10:
                notas.append(valida_nota)

            escolha = str(input('Quer inserir outra nota? (Sim/Não): ')).strip().upper()[0]
            if escolha in 'SN':
                if escolha == 'N':
                    break

        print(calcula_media(notas))
        break

    except Exception as e:
        print(f'Erro {e}, tente novamente')
