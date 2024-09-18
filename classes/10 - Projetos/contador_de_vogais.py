"""
Contador de vogais - Digite uma string e o programa conta o número de vogais no texto. Para maior complexidade,
informe a soma de cada vogal encontrada.
"""
from collections import Counter


def vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    formatted_string = string.strip().lower()
    vogais_string = list()
    count = 0
    counter = Counter(string)
    # count_vogal_a = counter['a']
    # count_vogal_e = counter['e']
    # count_vogal_i = counter['i']
    # count_vogal_o = counter['o']
    # count_vogal_u = counter['u']

    for letter in formatted_string:
        if letter in vogais:
            print(f'\t- Achei: {letter} ')
            count += 1
            vogais_string.append(letter)

    print()
    print('Analisando quantas vogais contêm:')
    for vogal in vogais_string:
        print(f'\tVogal: {vogal}, apareceu: {counter[vogal]}x')

    print()
    if count == 1:
        return f'Há \033[4m{count}\033[m vogal na string: \033[36m{string}\033[m'
    if count > 1:
        return f'Há \033[4m{count}\033[m vogais na string: \033[36m{string}\033[m'
    return f'A string: \033[36m{string}\033[m, não há vogais.'


try:
    string_user = str(input('Informe uma string: '))
    print(vogais(string_user))

except Exception as error:
    print(f'Ops: {error}')
