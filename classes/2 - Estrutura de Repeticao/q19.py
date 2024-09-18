"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""


def numero(* num):
    lista = num[0]
    return f'\nMenor: {min(lista)}' \
           f'\nMaior: {max(lista)}' \
           f'\nSoma:  {sum(lista)}'


while True:
    try:
        lista_num = []
        while True:
            num = int(input('Informe um número \033[34m(entre 0 e 1000)\033[m ou \033[36m"999" para parar\033[m: '))

            if num != 999 and 0 <= num <= 1000:
                lista_num.append(num)
            else:
                break

    except Exception as e:
        print(e)

    else:
        print(numero(lista_num))
        break
