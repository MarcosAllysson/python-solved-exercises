"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
"""

while True:
    try:
        while True:
            username = str(input('Informe o seu nome de usuário: '))
            password = str(input('Informe a sua senha: '))

            if username != password and username not in password:
                break
            print('\nUsuário e senha \033[36mnão podem ser iguais e nem conter usuário na senha!\033[m'
                  '\n \033[1;31mEXEMPLO DO QUE É PROIBIDO\033[m: Username: usuario, senha: usuario123'
                  '\n \033[1;34mEXEMPLO DO QUE É ACEITO\033[m: Username: usuario, senha: 34*As)-=')

    except Exception as error:
        print(f'Erro: {error}, tente novamente...')

    else:
        print(f'Usuário: \033[33m{username}\033[m e senha: \033[33m{password}\033[m válidos!')
        break
