def numero_inteiro(numero):
    """
    Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades
    """
    #  divisão inteira do número por 100
    centena = numero // 100

    #  divisão inteira do número por 10, do resto da divisão do número por 100
    dezena  = (numero % 100) // 10

    #  divisão inteira do número por 1, do resto da divisão do número por 10
    unidade = (numero % 10) // 1

    return f'{numero} = {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s).'


while True:
    try:
        while True:
            numero = int(input('Informe um número inteiro menos que 1000: '))
            if 0 <= numero < 1000:
                break
            print('\033[31mErro!\033[m Número entre 1 e 1000 somente! ')

    except Exception as error:
        print(f'Error: {error.__class__}, descrição: {error}.\n Tente novamente')

    else:
        print(numero_inteiro(numero))
        break

# testes = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
