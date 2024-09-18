"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""


def media_alunos(dict_alunos):
    qnt_turmas = qnt_alunos = 0

    for alunos in dict_alunos.values():
        qnt_turmas += 1
        qnt_alunos += alunos

    calculando_media_alunos = qnt_alunos // qnt_turmas

    return f'\n \033[1;36mExistem {qnt_turmas} turmas, e a média de alunos é de {calculando_media_alunos} alunos por turma.\033[m'


while True:
    try:
        turmas = dict()
        quantidade_turmas = int(input('Existem quantas turmas? '))

        for turma in range(1, quantidade_turmas+1):
            while True:
                valida_quantidade = int(input(f'Quantos alunos na turma {turma}? '))
                if 0 <= valida_quantidade <= 40:
                    turmas[f'turma_{turma}'] = valida_quantidade
                    break
                print('\033[31mA turma pode ter somente no máximo 40 alunos.\033[m')

    except Exception as e:
        print(e)

    else:
        print(media_alunos(turmas))
        break
