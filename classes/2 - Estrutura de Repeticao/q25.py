"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""


def media_idade(* idades):
    idade = []
    for n in idades[0]:
        idade.append(n)

    media_das_idades = sum(idade) / len(idade)
    if 0 <= media_das_idades <= 25:
        return f'\n \033[32mÉ uma turma jovem com média de:\033[m {media_das_idades:.2f} anos.'
    elif 26 <= media_das_idades <= 60:
        return f'\n \033[32mÉ uma turma adulta com média de:\033[m {media_das_idades:.2f} anos.'
    else:
        return f'\n \033[32mÉ uma turma idosa com média de:\033[m {media_das_idades:.2f} anos.'


while True:
    try:
        idades = []
        while True:
            valida_idades = float(input('Informe idade: '))
            if 1 <= valida_idades <= 150:
                idades.append(valida_idades)

            escolha = str(input('Quer inserir outra idade? (Sim/Não): ')).strip().upper()[0]
            if escolha in 'SN':
                if escolha == 'N':
                    break

        print(media_idade(idades))
        break

    except Exception as e:
        print(f'Erro {e}, tente novamente')
