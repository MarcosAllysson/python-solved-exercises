"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
alto e o número do aluno mais baixo, junto com suas alturas.
"""


def alunos(lista_alunos):
    for chave, aluno in enumerate(lista_alunos):
        #print(f'{aluno["aluno"]}, altura: {aluno["altura"]}m')
        print(f'{chave}: {aluno}')

    return f'{lista_alunos}'


dicio_alunos = dict()
lista_alunos = list()

#for alunos in range(1, 11):
for alunos in range(1, 6):
    dicio_alunos[f'aluno{alunos}'] = alunos
    dicio_alunos[f'altura{alunos}'] = float(input(f'Altura do aluno {alunos}: '))
    lista_alunos.append(dicio_alunos.copy())
    dicio_alunos.clear()

alunos(lista_alunos)
