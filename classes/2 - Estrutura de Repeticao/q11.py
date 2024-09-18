from time import sleep
from functools import reduce
"""
Altere o programa anterior para mostrar no final a soma dos números.
"""


def mostra_inteiros(comeco, fim):
    mensagem_1 = f'Começando do {comeco}, temos:'
    intervalo = [i for i in range(comeco+1, fim)]
    mensagem_2 = f'Terminando com {fim} =D.'

    # soma_dos_numeros = sum(intervalo) + comeco + fim
    intervalo.append(comeco)
    intervalo.append(fim)
    soma_dos_numeros = reduce(lambda a, b: a + b, intervalo)

    return f'\n{mensagem_1} \n{intervalo} \n{mensagem_2}\nSoma: {soma_dos_numeros}'


while True:
    try:
        while True:
            comeco = int(input('Informe onde começa: '))
            fim = int(input('Informe onde termina: '))
            if comeco < fim:
                break
            print('O começo precisa ser menor que o final!')

        print('\n \033[1;33mAnalisando...\033[m')
        sleep(3)

    except Exception as e:
        print(f'{e}.')

    else:
        print(mostra_inteiros(comeco, fim))
        break

