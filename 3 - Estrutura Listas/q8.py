"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

try:
    pessoas = list()

    for pessoa in range(5):
        pessoa_temporaria = []

        while True:
            idade = int(input(f'Idade da pessoa {pessoa + 1}: '))
            altura = float(input(f'Altura da pessoa {pessoa + 1}: '))

            if 1 <= idade <= 150 and 0.50 <= altura <= 2.70:
                pessoa_temporaria.append(idade)
                pessoa_temporaria.append(altura)
                break
            print(f'\n \033[31m Idade: entre 1 e 150. Altura entre 0.50 e 2,70m. \033[m')

        # copiando pessoa temporaria na lista geral
        pessoas.append(pessoa_temporaria[:])

        # limpando lista temporária
        pessoa_temporaria.clear()

        # quebrando linha
        print()

    # imprimindo pessoas
    pessoas.reverse()
    for chave, pessoa in enumerate(pessoas):
        print(f' -> Pessoa {chave+1}: tem {pessoa[0]} anos e {pessoa[1]:.2f}m de altura.')

except Exception as erro:
    print(f'{erro}')
