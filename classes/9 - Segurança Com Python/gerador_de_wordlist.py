"""
Programa que gera wordlist com biblioteca itertools.
"""

import itertools

string = str(input('String a ser permutada: ')).strip()

#  recebe a permutação dos caracteres formada de 3 caracteres ou pelo tamanho da string recebida
resultado = itertools.permutations(string, len(string))

# pra cada palavra formanada, concatena ao espaço vazio e printa
for palavra in resultado:
    print(''.join(palavra))
