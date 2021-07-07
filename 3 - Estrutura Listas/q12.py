"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.
"""

try:
    alunos = []
    for aluno in range(30):
        aluno_temporario = []

        while True:
            idade = int(input(f'Idade do aluno {aluno+1}: '))
            altura = float(input(f'Altura do aluno {aluno+1}: '))
            if 2 <= idade <= 100 and 0.50 <= altura <= 2.80:
                aluno_temporario.append(idade)
                aluno_temporario.append(altura)
                break
            print('\nIdade entre 2 e 100. Altura entre 0,50 e 2,80m')

        alunos.append(aluno_temporario[:])
        aluno_temporario.clear()
        print()

except Exception as erro:
    print(erro)

else:
    soma_altura = alunos_total = alunos_altura_inferior = 0

    for chave, aluno in enumerate(alunos):
        print(f'Aluno {chave+1} - tem {aluno[0]} anos e {aluno[1]:.2f}m.')
        soma_altura += aluno[1]
        alunos_total += 1

    # Calculando média
    media_dos_alunos = soma_altura / alunos_total

    for aluno in alunos:
        if aluno[0] > 13 and aluno[1] < media_dos_alunos:
            alunos_altura_inferior += 1

    print(f'\nHá {alunos_total} alunos.'
          f'\nSala tem média de {media_dos_alunos:.2f}m de altura'
          f'\nE {alunos_altura_inferior} possuem altura inferior a média dos alunos totais.')

finally:
    print('\n \033[32mAté breve!\033[m')
