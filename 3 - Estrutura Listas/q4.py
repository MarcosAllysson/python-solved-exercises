import string


def conta_consoantes(consoantes):
    """
    Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
    """
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista_consoantes = list()
    cont = 0

    for caracter in consoantes:
        if caracter.lower() not in vogais:
            cont += 1
            lista_consoantes.append(caracter)

    return f'Foram encontrados {cont} consoantes, e são: {lista_consoantes}.'


try:
    vetor_caracteres = list()

    for vetor in range(10):
        while True:
            caracter = str(input(f'Informe {vetor+1}° caracter: '))[0]
            if caracter in string.ascii_letters:
                vetor_caracteres.append(caracter)
                break
            print('\033[31mCaracter inválido! Somente de A - Z.\033[m')

    print(conta_consoantes(vetor_caracteres))

except Exception as erro:
    print(erro)
