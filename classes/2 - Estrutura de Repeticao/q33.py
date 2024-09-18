"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""


def temperatura(temps):
    return f'\nMenor temperatura: {min(temps)}°' \
           f'\nMaior temperatura: {max(temps)}°' \
           f'\nMédia: {sum(temps) / len(temps):.2f}°'


try:
    temps = list()
    while True:
        temp = float(input('Informe a temperatura OU 0 para parar: '))

        if temp == 0:
            break
        else:
            temps.append(temp)

    print(temperatura(temps))

except:
    print('Erro, tente novamente.')
