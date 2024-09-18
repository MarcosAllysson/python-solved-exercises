"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""


def gerador_de_tabuada(numero):
    print(f'\n \033[32mGerando tabuada de {numero}...\033[m')
    for num in range(0, 11):
        print(f'{numero} x {num} = {numero * num}')


while True:
    try:
        print('\033[34mGerador de Tabuada:\033[m ')
        while True:
            numero = int(input('Informe um valor entre 1 e 10 pra eu gerar a tabuada: '))
            if 1 <= numero < 11:
                break
            print('\033[1;31mErro! Somente número inteiro 1-10.\033[m')

    except Exception as error:
        print(f'{error}.')

    else:
        gerador_de_tabuada(numero)
        break
