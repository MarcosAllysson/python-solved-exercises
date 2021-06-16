"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""


def conceito_de_nota():
    print('\033[1;36mMédia de Aproveitamento | Conceito\033[m \n'
          '  \033[1;32mEntre: 9.0 e 10.0           A\033[m \n'
          '  \033[1;32mEntre: 7.5 e 9.0            B\033[m \n'
          '  \033[1;32mEntre: 6.0 e 7.5            C\033[m \n'
          '  \033[1;32mEntre: 4.0 e 6.0            D\033[m \n'
          '  \033[1;32mEntre: 4.0 e zero           E\033[m \n')


def calcula_media(primeira_nota, segunda_nota):
    # printando conceito geral das notas
    conceito_de_nota()

    # calculando média
    media_das_notas = (primeira_nota + segunda_nota) / 2

    # retornando mensagem final após verificação:
    if 9.0 <= media_das_notas <= 10:
        return f'\033[1;36mMédia final do aluno:\033[m \n' \
               f'Notas: {primeira_nota:.1f} e {segunda_nota:.1f}\n' \
               f'Média: {media_das_notas:.1f}\n' \
               f'Conceito: A\n' \
               f'Mensagem: Aprovado!'

    elif 7.5 <= media_das_notas <= 9:
        return f'\033[1;36mMédia final do aluno:\033[m \n' \
               f'Notas: {primeira_nota:.1f} e {segunda_nota:.1f}\n' \
               f'Média: {media_das_notas:.1f}\n' \
               f'Conceito: B\n' \
               f'Mensagem: Aprovado'

    elif 6 <= media_das_notas < 7.5:
        return f'\033[1;36mMédia final do aluno:\033[m \n' \
               f'Notas: {primeira_nota:.1f} e {segunda_nota:.1f}\n' \
               f'Média: {media_das_notas:.1f}\n' \
               f'Conceito: C\n' \
               f'Mensagem: Aprovado'

    elif 4 <= media_das_notas < 6:
        return f'\033[1;36mMédia final do aluno:\033[m \n' \
               f'Notas: {primeira_nota:.1f} e {segunda_nota:.1f}\n' \
               f'Média: {media_das_notas:.1f}\n' \
               f'Conceito: D\n' \
               f'Mensagem: Reprovado'

    else:
        return f'\033[1;36mMédia final do aluno:\033[m \n' \
               f'Notas: {primeira_nota:.1f} e {segunda_nota:.1f}\n' \
               f'Média: {media_das_notas:.1f}\n' \
               f'Conceito: E\n' \
               f'Mensagem: Reprovado'


#  programa principal
while True:
    try:
        while True:
            primeira_nota = float(input('Digite a 1° nota: '))
            segunda_nota  = float(input('Digite a 2° nota: '))

            if 0 <= primeira_nota <= 10 and 0 <= segunda_nota <= 10:
                break
            print('Notas inválidas! Aceito somente entre 0 e 10.')

    except Exception as error:
        print(f'Erro: {error.__class__}, {error}.')

    else:
        print(calcula_media(primeira_nota, segunda_nota))
        break
