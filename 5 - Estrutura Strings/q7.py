"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""


def conta_espacos_vogais():
    qnt_brancos = qnt_vogais = 0
    vogais = ['a', 'e', 'i', 'o', 'u']

    frase = str(input('Digite uma frase: ')).lower()

    for letra in frase:
        if letra == ' ':
            qnt_brancos += 1
        if letra in vogais:
            qnt_vogais += 1

    print(f'\nA frase: \033[36m"{frase}"\033[m, têm {qnt_brancos} espaços em branco e {qnt_vogais} vogais.')


if __name__ == '__main__':
    conta_espacos_vogais()
