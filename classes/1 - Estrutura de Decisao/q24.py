def operacao(lista_num, funcao):
    """
    Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
    O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
    """
    if funcao == 1:
        resultado = list(map(lambda x: x % 2 == 0, lista_num))
        return f'{resultado}, respectivamente.'

    elif funcao == 2:
        resultado = list(map(lambda x: x >= 0, lista_num))
        return f'{resultado}, respectivamente'

    elif funcao == 3:
        resultado = list(map(lambda x: x == round(x), lista_num))
        return f'{resultado}, respectivamente'


while True:
    try:
        lista_num = []
        for i in range(2):
            lista_num.append(float(input(f'Informe o {i + 1}° número: ')))

        while True:
            funcao = int(input(f'Qual opção deseja realizar? \n'
                               f'1 - Par ou ímpar; \n'
                               f'2 - Positivo ou negativo; \n'
                               f'3 - Inteiro ou decimal; \n'
                               f'Sua escolha: '))
            if funcao == 1 or funcao == 2 or funcao == 3:
                break
            print('Opção inválida!.')

    except:
        print('Houve um erro, tenta de novo...')

    else:
        print(operacao(lista_num, funcao))
        break
