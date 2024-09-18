"""
Conte as palavras em uma string - Conta o número de palavras individuais em uma string. Para maior complexidade,
leia essas sequências a partir de um arquivo de texto e gere um resumo.
"""


def count_words_string(string):
    list_string = string.split()
    return f'Number of words found: {len(list_string)}.'


try:
    string = str(input('Type a string: ')).strip()
    print(count_words_string(string))

except Exception as error:
    print(f'{error}')
