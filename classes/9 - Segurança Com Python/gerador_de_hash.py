import hashlib
"""
Programa gerador de hash md5, sha1, sha256 e sha512
"""

#  converte em bytes a string para md5
#resultado = hashlib.md5(b'Python3 programming language')


while True:
    try:
        string = str(input('Digite um texto para gerar hash: '))
        while True:
            menu = int(input('MENU - ESCOLHA O TIPO DE HASH: \n'
                         '1 - MD5\n'
                         '2 - SHA1\n'
                         '3 - SHA256\n'
                         '4 - SHA512\n'
                         'Digite o número de sua escolha: '))
            if menu == 1 or menu == 2 or menu == 3 or menu == 4:
                break
            print('\033[31mOpção inválida! Escolha somente entre 1 e 4!\033[m ')

    except Exception as error:
        print(f'Erro: {error.__class__}, descrição: {error}.\nTente novamente.')

    else:
        if menu == 1:
            resultado = hashlib.md5(string.encode('utf-8'))
            print(f'O hash MD5 da string \033[4m"{string}"\033[m é: {resultado.hexdigest()}')
            break
        elif menu == 2:
            resultado = hashlib.sha1(string.encode('utf-8'))
            print(f'O hash SHA1 da string \033[4m"{string}"\033[m é: {resultado.hexdigest()}')
            break
        elif menu == 3:
            resultado = hashlib.sha256(string.encode('utf-8'))
            print(f'O hash SHA256 da string \033[4m"{string}"\033[m é: {resultado.hexdigest()}')
            break
        else:
            resultado = hashlib.sha512(string.encode('utf-8'))
            print(f'O hash SHA512 da string \033[4m"{string}"\033[m é: {resultado.hexdigest()}')
            break
