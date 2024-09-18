from time import sleep


def calcula_media(notas):
    """
    Programa para leitura de três notas parciais de um aluno. O programa calcula a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
    """
    media_notas = sum(notas) / len(notas)

    if media_notas == 10:
        return f'\nAprovado com Distinção. \nNota: {media_notas:.1f}'
    elif media_notas >= 7:
        return f'\nAprovado. \nNota: {media_notas:.1f}'
    else:
        return f'\nReprovado. \nNota: {media_notas:.1f}'


while True:
    try:
        notas = list()

        for i in range(3):
            while True:
                nota = float(input(f'Informe a {i+1}° nota: '))

                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                print('Nota inválida! Insira nota somente entre 0 e 10 (incluído)')

        print(f'\nNotas recebidas: {notas}. \nCalculando sua média final...')
        sleep(2)

    except Exception as error:
        print(f'Error: {error.__class__}, descrição: {error}.')

    else:
        print(calcula_media(notas))
        break
