"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""


def eleicao(votos):
    return f'\n \033[32mAPURAÇÃO ELEIÇÃO:\033[m ' \
           f'\nCandidato A teve: {votos.count(1)} votos;' \
           f'\nCandidato B teve: {votos.count(2)} votos;' \
           f'\nCandidato C teve: {votos.count(3)} votos;'


while True:
    try:
        lista_votos = list()
        numero_total_eleitores = int(input('Qual número total de eleitores? '))

        for eleitor in range(numero_total_eleitores):
            while True:
                voto = int(input(f'\n#{eleitor+1}° VOTO: Escolha o número do seu candidato:'
                                 '\n1 - Candidato A'
                                 '\n2 - Candidato B'
                                 '\n3 - Candidato C'
                                 '\nSua escolha: '))
                if 1 <= voto <= 3:
                    lista_votos.append(voto)
                    break
                print('\033[1;31mOpção inválida, somente 1, 2 e 3 são votos válidos.\033[m')

    except Exception as e:
        print(f'{e}')

    else:
        print(eleicao(lista_votos))
        break
