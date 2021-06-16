"""
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""

while True:
    try:
        numero = int(input('Digite um número: '))
    except Exception as error:
        print(f'Erro: {error}')
    else:
        print(f'O número informado foi {numero}')
        break
