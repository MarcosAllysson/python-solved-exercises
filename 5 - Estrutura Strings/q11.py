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


while True:
    palavra = 'JESUS'
    palavra_temp = list()

    letra = str(input('Digite uma letra: ')).strip().upper()[0]

    if letra in palavra:
        palavra_temp.append(letra)

    else:
        print('Errou!')

    print(palavra_temp)



