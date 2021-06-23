"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário.
"""

# 1995 = 1.000
# 1996 = + 1.5%
# 1997 = ano anterior * 2


def aumento_salarial(r):
    salario_inicial = 1000
    desconto_inicial = 0.015
    desconto_seguinte = desconto_inicial * 2

    for i in range(r):
        print(f'Salário inicial: R$ {salario_inicial}')
        print(f'Desconto inicial: {desconto_inicial}, novo salário acrescenta: R$ {salario_inicial * desconto_inicial}')
        print(f'Salário ano seguinte aumenta: R$ {salario_inicial * desconto_seguinte}')
        print()


aumento_salarial(2)

