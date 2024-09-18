def fatorial(num=1):
    """
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
    Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
    """
    fatorial_de_num = 1
    print(f'Fatorial de: {num}')

    print(f'{num}! = ', end='')
    for i in range(num, 0, -1):
        fatorial_de_num *= i
        print(f'{i}', end='')
        if i > 1:
            print(' . ', end='')
        else:
            print(' = ', end='')

    return fatorial_de_num


try:
    numero_usuario = int(input('Informe um número: '))
    print(fatorial(numero_usuario))
except:
    print('Erro, tente novamente.')
