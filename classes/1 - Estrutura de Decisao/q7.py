from functools import reduce


def maior_menor_numero_lido(* valores):
    """
    Programa que lê três números e retorna o maior e o menor deles.
    """
    numeros = list()

    for valor in valores[0]:
        numeros.append(valor)

    #  result é uma tupla com 2 índíces, no qual o índice 0 recebe o maior, e o índice 1, o menor valor.
    result = (reduce(lambda a, b: a if (a > b) else b, numeros), reduce(lambda a, b: a if (a < b) else b, numeros))
    return f'O maior número digitado foi o {result[0]}, e o menor: {result[1]}.'
    #  outra opção: max(numeros), min(numero)


while True:
    try:
        numeros = []

        for i in range(3):
            numeros.append(float(input(f'Digite o {i+1}° número: ')))

        print(f'Ok, números lidos foram: {numeros}.')

    except Exception as error:
        print(f'Ops, houve um erro: {error}\nTenta de novo!')

    else:
        print(f'{maior_menor_numero_lido(numeros)}')
        break
