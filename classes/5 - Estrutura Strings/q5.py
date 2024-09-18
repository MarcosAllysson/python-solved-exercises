"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""


def name(str):
    for letter in range(len(str), 0, -1):
        print(str[:letter])


try:
    while True:
        user_name = str(input('Qual seu nome? ')).strip().upper()
        if len(user_name) > 0:
            name(user_name)
            break
        print('Informe um nome com pelo menos 1 letra.')

except Exception as error:
    print(error)
