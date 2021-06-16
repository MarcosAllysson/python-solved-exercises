"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""


def reajuste_salarial(salario):
    """
    Programa que calcula reajuste salarial de 5 a 20%
    """
    if salario > 1500:
        return f'Salário antes do reajuste: R$ {salario:.2f}' \
               f'\nPercentural de aumento aplicado: 5%' \
               f'\nValor do aumento: R$ {salario * 0.05:.2f}' \
               f'\nNovo salário, após o aumento: {salario + (salario * 0.05):.2f}'
    elif salario > 700 and salario <= 1500:
        return f'Salário antes do reajuste: R$ {salario:.2f}' \
               f'\nPercentural de aumento aplicado: 10%' \
               f'\nValor do aumento: R$ {salario * 0.10:.2f}' \
               f'\nNovo salário, após o aumento: {salario + (salario * 0.10):.2f}'
    elif salario > 280 and salario <= 700:
        return f'Salário antes do reajuste: R$ {salario:.2f}' \
               f'\nPercentural de aumento aplicado: 15%' \
               f'\nValor do aumento: R$ {salario * 0.15:.2f}' \
               f'\nNovo salário, após o aumento: {salario + (salario * 0.15):.2f}'
    else:
        return f'Salário antes do reajuste: R$ {salario:.2f}' \
               f'\nPercentural de aumento aplicado: 20%' \
               f'\nValor do aumento: R$ {salario * 0.20:.2f}' \
               f'\nNovo salário, após o aumento: {salario + (salario * 0.20):.2f}'


while True:
    try:
        salario = float(input('Informe seu salário para calcularmos o reajuste: R$ '))

    except Exception as error:
        print(f'Erro: {error.__class__}, descrição: {error}.')

    else:
        print(reajuste_salarial(salario))
        break
