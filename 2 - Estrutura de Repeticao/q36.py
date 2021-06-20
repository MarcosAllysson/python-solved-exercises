"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""


def tabuada(numero, inicio=1, final=10):
    print(f'\n \033[36mVou montar a tabuada de {numero} começando em {inicio} e terminando em {final}:\033[m ')
    for num in range(inicio, final+1):
        print(f'{numero} x {num} = {numero * num}')


# programa principal
while True:
    try:
        # validando números
        while True:
            numero = int(input('Informe número da tabuada: '))
            inicio = int(input('Quer começar em qual número? '))
            final = int(input('Quer terminar em qual número? '))

            if (1 <= numero <= 10) and (1 <= inicio <= 10) and (1 <= final <= 10) and (inicio < final):
                tabuada(numero, inicio, final)
                break
            print('\n \033[31mErro: insira somente de 1 a 10, e o final menor que o começo! \033[m')

        # saindo do loop
        break

    except:
        print('Erro, tente novamente...')
