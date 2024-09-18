"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

while True:
    try:
        ganho_por_hora = float(input('Quanto você ganha por hora? R$ '))
        horas_trabalhada_mes = int(input('Trabalha quantas horas por mês? '))
        salario_bruto = ganho_por_hora * horas_trabalhada_mes

        # 11% para o Imposto de Renda
        reducao_ir = salario_bruto - (salario_bruto * 0.11)

        # 8% para o INSS 
        reducao_inss = reducao_ir - (reducao_ir * 0.08)

        # 5% para o sindicato
        reducao_sindicato = reducao_inss - (reducao_inss * 0.05)

        # desconto
        descontos = (salario_bruto * 0.11) + (reducao_ir * 0.08) + (reducao_inss * 0.05)

        # salário líquido
        salario_liquido = salario_bruto - descontos

    except Exception as error:
        print(f'Erro: {error.__class__}, descrição: {error}.')

    else:
        print(f'\nGanha por hora: R$ {ganho_por_hora}, trabalha {horas_trabalhada_mes}h por mês.\n\033[36mTABELA:\033[m')
        print(f"""
        + Salário Bruto    : R$ {salario_bruto:>10.2f}
        - IR (11%)         : R$ {reducao_ir:>10.2f}
        - INSS (8%)        : R$ {reducao_inss:>10.2f}
        - Sindicato (5%)   : R$ {reducao_sindicato:>10.2f}
        \033[1;32m- Descontos Totais : R$ {descontos:>10.2f}\033[m

        \033[33m= Salário Liquido  : R$ {salario_liquido:>10.2f}\033[m
        \033[36mObs.: Salário Bruto - Descontos = Salário Líquido\033[m.""")
        break
