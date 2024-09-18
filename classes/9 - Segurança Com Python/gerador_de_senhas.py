import random
import string
from time import sleep

while True:
    try:
        #  perguntando ao usuário o tamanho da senha desejada. Aceitável no mínimo 6 caracteres
        while True:
            tamanho = int(input('Digite o tamanho de senha que você quer: '))
            if tamanho > 5:
                break
            print('\033[1;31mPara sua segurança, tamanho mínimo: 6 caracteres.\033[m')

        #  junção de caracteres maiúsculos e minúsculo, dígitos de 0 a 9 e caracteres especiais.
        caracteres = string.ascii_letters + string.digits + 'çÇ!@#$%&*()_-+=.;/°^~[]{}?|:<>'

        #  geração de aleatórios
        rnd = random.SystemRandom()  # os.urandom()

        #  Num range de tamanho, escolhe um caracter de caracteres, concatenando ao espaço vazio.
        senha_gerada = ''.join(rnd.choice(caracteres) for i in range(tamanho))

        #  Sleep de 3 segundos
        print('Gerando senha...')
        sleep(3)

    except Exception as error:
        print(f'Houve um erro: {error.__class__}, descrição: {error}.')

    else:
        print(f'\033[1;31mSenha gerada, guarde num local seguro:\033[m {senha_gerada}')
        break
