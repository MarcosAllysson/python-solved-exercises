from time import sleep


def ordem_decrescente(valor1=0, valor2=0, valor3=0):
    """
    Programa que lê três números e mostre-os em ordem decrescente.
    """
    numeros = [valor1, valor2, valor3]
    numeros.sort(reverse=True)
    return numeros


while True:
    try:
        primeiro_valor = float(input('Informe o 1° número: '))
        segundo_valor = float(input('Informe o 2° número: '))
        terceiro_valor = float(input('Informe o 3° número: '))

        print(f'Certo, valores digitados foram: {primeiro_valor, segundo_valor, terceiro_valor}. Vamos analisar...')
        sleep(2)

    except Exception as error:
        print(f'Ops, erro: {error}.\nTenta de novo!')

    else:
        print(f'Ordem decrescente dos valores informados: '
              f'{ordem_decrescente(primeiro_valor, segundo_valor, terceiro_valor)}')
        break
