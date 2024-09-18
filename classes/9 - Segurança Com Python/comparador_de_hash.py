import hashlib

#  necessários ter 2 arquivos para comparação
#comparador_de_hash_primeiro_arquivo.txt
#comparador_de_hash_segundo_arquivo.txt

primeiro_arquivo = 'comparador_de_hash_primeiro_arquivo.txt'
segundo_arquivo = 'comparador_de_hash_segundo_arquivo.txt'

# definindo algoritmo de hash: ripemd160
hash1 = hashlib.new('ripemd160')

# informando qual arquivo a ser aberto pra comparação
hash1.update(open(primeiro_arquivo, 'rb').read())

# definindo hash do 2° arquivo
hash2 = hashlib.new('ripemd160')
hash2.update(open(segundo_arquivo, 'rb').read())

# comparação
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {primeiro_arquivo} é \033[31mDIFERENTE\033[m do arquivo: {segundo_arquivo}')
    print(f'O hash do 1° arquivo é: {hash1.hexdigest()}')
    print(f'O hash do 2° arquivo é: {hash2.hexdigest()}')
else:
    print(f'O arquivo: {primeiro_arquivo} é \033[31mIGUAL\033[m do arquivo: {segundo_arquivo}')
    print(f'O hash do 1° arquivo é: {hash1.hexdigest()}')
    print(f'O hash do 2° arquivo é: {hash2.hexdigest()}')
