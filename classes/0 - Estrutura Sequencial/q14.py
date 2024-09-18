"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido 
pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 
por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável 
multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

while True:
    try:
        peso = float(input('Informe o peso: '))

        if peso > 50:
            excesso = peso - 50
            multa = excesso * 4

            msg = f'O limite é de 50kg, você ultrapassou {excesso:.2f}kg, multa de R$ 4,00 por kilo - TOTAL: R$ {multa:.2f}.'
        else:
            msg = f'Você está dentro do limite de 50kg, não tens nada a pagar.'

    except Exception as error:
        print(f'Erro {error.__class__}, descrição: {error}.')

    else:
        print(f'{msg}')
        break
