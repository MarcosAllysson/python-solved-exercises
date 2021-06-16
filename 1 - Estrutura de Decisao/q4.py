def eh_vogal_ou_consoante(letra):
    """
    Programa que verifiqua se uma letra digitada é vogal ou consoante.
    """
    vogais = ['A', 'E', 'I', 'O', 'U']

    if letra in vogais:
        return f'\033[36m{letra}\033[m, é uma vogal.'
    else:
        return f'\033[36m{letra}\033[m, é uma consoante.'


while True:
    """
    Programa validando se foi digitado somente uma letra, tratando erro e invocando função. 
    """
    try:
        while True:
            letra = str(input('Digite uma letra: ')).strip().upper()
            if len(letra) == 1 and letra.isalpha():
                break
            print('Informe apenas uma letra! Vamos de novo.')

    except Exception as error:
        print(f'Ops, {error}.\nTente novamente!')

    else:
        print(eh_vogal_ou_consoante(letra))
        break
