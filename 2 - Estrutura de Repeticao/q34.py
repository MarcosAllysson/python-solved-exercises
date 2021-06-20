def primo(num=1):
    """
    Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
    que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
    um número primo.
    """
    divisores = 0

    for i in range(1, num+1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        return True
    else:
        return False


try:
    while True:
        numero = int(input('Informe um número inteiro: '))
        if numero >= 0:
            if primo(numero):
                print(f'{numero} é primo.')
            else:
                print(f'{numero} não é primo.')

            # parando programa.
            break

        # caso número recebido seja negativo.
        print('Somente números inteiros maior ou igual a 0.')
except:
    print('Erro, tente novamente.')
