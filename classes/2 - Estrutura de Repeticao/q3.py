"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    try:
        while True:
            nome = str(input('Informe seu nome: ')).strip().title()
            if len(nome) > 3 and nome.isalpha():
                break
            print('Nome deve possuir no mínimo 3 caracteres e devem ser letras!')

        while True:
            idade = int(input('Informe sua idade: '))
            if 0 <= idade <= 150:
                break
            print('Idade permitida: entre 0 e 150 somente! ')

        while True:
            salario = float(input('Salário: R$ '))
            if salario > 0:
                break
            print('Salário precisa ser maior que 0')

        while True:
            sexo = str(input('Sexo: [F ou M]: ')).strip().upper()[0]
            if sexo in 'FM':
                break
            print('Insira somente F para feminino ou M para masculino.')

        while True:
            estado_civil = str(input('Estado civil, considerando: '
                                     '\nS - Solteiro '
                                     '\nC - Casado '
                                     '\nV - Viúvo '
                                     '\nD - Divorciado'
                                     '\nSua opção: ')).strip().upper()[0]
            if estado_civil in 'SCVD':
                break
            print('Insira somente as siglas conforme explicação: S, C, V ou D.')

    except Exception as error:
        print(f'Error: {error}, tente novamente...')

    else:
        print(f'\n \033[36mInformações validadas com sucesso:\033[m '
              f'\nNome: {nome}'
              f'\nIdade: {idade}'
              f'\nSalário: R$ {salario:.2f}'
              f'\nSexo: {sexo}'
              f'\nEstado civil: {estado_civil}')
        break
