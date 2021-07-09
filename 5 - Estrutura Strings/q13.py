"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o
usuário ganhou ou perdeu o jogo.
"""


from random import shuffle, choice
from time import sleep

word_list = [
    'churrasco',
    'ferradura',
    'sorriso',
    'faqueiro',
    'periquito',
    'baralho',
    'tartaruga',
    'grande',
    'brincadeira',
    'passagem',
    'vassoura',
    'cheirosa',
    'avestruz',
    'xadrez',
    'guerreiro',
    'formigueiro',
    'guitarra',
    'caranguejo',
    'avental',
    'impressora',
    'chiclete',
    'bicicleta',
    'inglesa',
    'surpresa'
]

word = choice(word_list)
new_word = []
tempts = 1

# Timer sleep 3 segundos
print('SORTEANDO PALAVRA...')
sleep(3)

# Pra cada letra da palavra, adiciono à lista
for letter in word.lower():
    new_word.append(letter)

# Embaralhando as letras
shuffle(new_word)

# Mostrando palavra embaralhada
print(f'\033[33mA palavra embaralhada é:\033[m -> ', end='')
for letter in new_word:
    print(f'\033[1;36m{letter}\033[m', end='')

# Jogo em si
print()
try:
    while tempts < 4:
        guess = str(input('\n \033[1;35mQual seu palpite?\033[m ')).strip().lower()

        if guess == word:
            print(f'\n \033[1;32m VOCÊ ACERTOUUUUUUUUUUUUUUU! A palavra é: {word}')
            quit()
        else:
            print(f'\n \033[31mERRADO! Você tem {3 - tempts} tentativas. \033[m')
            tempts += 1

    print(f'\n QUE PENAAAAAAAAAAAA! A palavra certa era: {word}')

except Exception as error:
    print(f'Ops, houve um erro no jogo {error.__class__}, descrição: {error}')
