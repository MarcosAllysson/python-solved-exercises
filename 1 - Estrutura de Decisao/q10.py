def cumprimento(turno='Valor Inválido!'):
    """
    Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
    """
    if turno == 'M':
        return 'Bom dia!'
    elif turno == 'V':
        return 'Boa tarde!'
    elif turno == 'N':
        return 'Boa Noite!'
    else:
        return 'Valor inválido!'


#  Programa principal
while True:
    try:
        turno = str(input('Em qual turno você estuda? '
                          '\nConsidere: M - Matutino, V - Vespertino ou N - Noturno: ')).lstrip().upper()[0]

    except Exception as error:
        print(f'Erro: {error}.\nTente novamente.')

    else:
        print(cumprimento(turno))
        break
