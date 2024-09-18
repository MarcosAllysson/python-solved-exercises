"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

from random import choice
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

# Timer sleep 3 segundos
print('SORTEANDO PALAVRA...')
sleep(3)
word = choice(word_list)


palavra_split = list()
letras_acertadas_usuario = list()
cont = 0

# Palavra secreta do jogo:
for letra in word:
    palavra_split.append(letra.upper())

# Preenchendo lista com traços:
for i in range(0, len(palavra_split)):
    letras_acertadas_usuario.append('_')

try:
    acertou = False

    while not acertou:
        print()  # quebrando linha
        letra = str(input('\nDigite uma letra: ')).strip().upper()[0]

        # Validando se é letra:
        if letra.isalpha():
            print(f'A palavra é: ', end=' ')

            for i in range(0, len(palavra_split)):
                if letra == palavra_split[i]:
                    letras_acertadas_usuario[i] = letra

                print(letras_acertadas_usuario[i], end=' ')

            acertou = True

            for x in range(0, len(letras_acertadas_usuario)):
                if letras_acertadas_usuario[x] == '_':
                    acertou = False

        # Diferente de letra, jogada inválida.
        else:
            print('Jogada inválida. Jogue somente letra.')

except IndexError:
    print('Espaços em branco não são permitidos.')

except TypeError:
    print('Jogada não permitida, tipo permitido: letra')

except Exception as error:
    print(f'Erro: {error.__class__}.')
