"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO
"""


def name(str):
    for letter in range(0, len(str) + 1):
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


