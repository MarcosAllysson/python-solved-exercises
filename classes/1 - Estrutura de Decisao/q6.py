from functools import reduce


def maior_numero_lido(* valores):
    """
    Programa que lê três números e retorna o maior deles.
    """
    numeros = list()

    for valor in valores[0]:
        numeros.append(valor)

    return reduce(lambda a, b: a if (a > b) else b, numeros)
    #  outra opção: max(numeros)


while True:
    try:
        numeros = []

        for i in range(3):
            numeros.append(float(input(f'Digite o {i+1}° número: ')))

        print(f'Ok, números lidos foram: {numeros}.')

    except Exception as error:
        print(f'Ops, houve um erro: {error}\nTenta de novo!')

    else:
        print(f'Maior número digitado foi: {maior_numero_lido(numeros)}.')
        break
