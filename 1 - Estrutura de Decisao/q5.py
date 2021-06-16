def calcula_media(* notas):
    """
    Programa faz a leitura de duas notas parciais de um aluno.
    O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
    """
    soma_notas = []

    for nota in notas[0]:
        soma_notas.append(nota)

    media_parcial = sum(soma_notas) / len(soma_notas)

    if media_parcial == 10:
        return f'Aprovado com distinção! Nota {media_parcial:.2f}'

    elif media_parcial >= 7:
        return f'Aprovado com nota {media_parcial:.2f}'

    else:
        return f'Reprovado com nota {media_parcial:.2f}'


while True:
    try:
        notas = []

        while True:
            primeira_nota = float(input('Digite a 1° nota: '))
            segunda_nota = float(input('Digite a 2° nota: '))

            if (primeira_nota >= 0 and primeira_nota <= 10) and (segunda_nota >=0 and segunda_nota <= 10):
                break
            print('Notas somente entre 0 e 10.')

        notas.append(primeira_nota)
        notas.append(segunda_nota)

    except Exception as error:
        print(f'Ops, {error}.')

    else:
        print(calcula_media(notas))
        break
