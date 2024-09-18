def media_notas(notas):
    """
    Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
    imprima o número de alunos com média maior ou igual a 7.0.
    """
    melhores_alunos = 0
    print('\n \033[36m MÉDIA DOS ALUNOS: \033[m \n')

    for aluno, nota in enumerate(notas):
        media = sum(nota) / len(nota)
        print(f'Aluno {aluno+1}, média: {media:.1f}')

        if media >= 7:
            melhores_alunos += 1

    return f'\n \033[33m APURAÇÃO FINAL: Há {melhores_alunos} alunos com nota igual ou maior que 7.0!\033[m'


try:
    notas = list()

    for n in range(10):
        nota_aluno = list()

        for na in range(4):
            while True:
                nota = float(input(f'Informe a {na+1}° nota do aluno {n+1}: '))
                if 0 <= nota <= 10:
                    nota_aluno.append(nota)
                    break
                print('\033[31mSomente entre 0 e 10.\033[m')

        print()
        notas.append(nota_aluno[:])
        nota_aluno.clear()

    print(media_notas(notas))

except:
    print('Erro, tente novamente...')
