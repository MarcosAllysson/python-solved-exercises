"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
"""


try:
    while True:
        nota = float(input('Informe um nota: '))
        if 0 <= nota <= 10:
            print(f'Nota válida: {nota}')
            break
        print('Aceito somente entre 0 e 10.')

except:
    print('Erro, tente novamente informando um número...')
