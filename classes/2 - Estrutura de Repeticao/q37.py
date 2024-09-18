"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""


def academia(lista_de_clientes):
    cont = 0
    mais_alto = mais_baixo = mais_gordo = mais_magro = 0
    soma_altura = soma_peso = 0

    for cliente in lista_de_clientes:
        print(f'Código: {cliente["codigo"]}')
        print(f'Altura: {cliente["altura"]:.2f}m')
        print(f'Peso: {cliente["peso"]:.2f} Kg')

        # Somando alturas e pesos
        soma_altura += cliente['altura']
        soma_peso += cliente['peso']

        # Analisando alturas
        if cont == 0:
            mais_alto = mais_baixo = cliente["altura"]
            mais_gordo = mais_magro = cliente["peso"]
        elif cliente["altura"] > mais_alto:
            mais_alto = cliente["altura"]
        elif cliente["altura"] < mais_baixo:
            mais_baixo = cliente["altura"]

        # Analisando pesos
        if cliente["peso"] > mais_gordo:
            mais_gordo = cliente["peso"]
        elif cliente["peso"] < mais_magro:
            mais_magro = cliente["peso"]

        # Contador
        cont += 1

    # calculando média:
    media_altura = soma_altura / cont
    media_peso = soma_peso / cont

    return f'\n \033[33m DADOS DOS CLIENTES: \033[m' \
           f'\nMais alto: {mais_alto:.2f}m' \
           f'\nMais baixo: {mais_baixo:.2f}m' \
           f'\nMais gordo: {mais_gordo:.2f}kg' \
           f'\nMais magro: {mais_magro:.2f}kg' \
           f'\nMédia das alturas: {media_altura:.2f}m' \
           f'\nMédia dos pesos: {media_peso:.2f}kg'


while True:
    try:
        lista_clientes = list()
        dado_cliente = dict()

        while True:
            dado_cliente['codigo'] = int(input('Digite o código do cliente: '))
            dado_cliente['altura'] = float(input('Informe a altura do cliente: '))
            dado_cliente['peso'] = float(input('E o peso: '))

            lista_clientes.append(dado_cliente.copy())

            while True:
                escolha = str(input('\nDigite "S" para inserir outro ou 0 para parar: ')).strip().upper()[0]
                if escolha in 'S0':
                    break
                print('\n \033[31mEscolha somente S ou 0.')

            if escolha == '0':
                break

    except Exception as error:
        print(f'Houve, erro. Tente novamente. \nErro: {error.__class__}, descrição: {error}.')

    else:
        print(academia(lista_clientes))
        break
