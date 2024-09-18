def verifica_sexo(sexo='desconhecido'):
    """
    Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
    """
    if sexo == 'F':
        return 'F - Feminino'
    elif sexo == 'M':
        return 'M - Masculino'
    else:
        return 'Sexo inválido.'


while True:
    try:
        sexo = str(input('Informe o sexo: (Feminino/Masculino): ')).strip().upper()[0]

    except Exception as error:
        print(f'Ops, {error}\nTente novamente!')

    else:
        print(verifica_sexo(sexo))
        break
