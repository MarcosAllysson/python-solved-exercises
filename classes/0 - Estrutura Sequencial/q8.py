"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

while True:
    """
    Cálculo: multiplicação do valor da hora x horas diárias
    Multiplicado por quantos dias trabalha por semana x 4 (referente ao mês ter 4 semanas)
    """
    try:
        ganho_por_hora = float(input('Quanto vc ganha por hora?\nR$ '))
        trabalha_horas_por_dia = int(input('Trabalha quantas horas por dia? '))
        trabalha_dias_por_semana = int(input('Trabalha quantos dias por semana? '))
        calculo_salario_mes = (ganho_por_hora * trabalha_horas_por_dia) * (trabalha_dias_por_semana * 4)
    except Exception as error:
        print(f'Não consegui calcular: {error.__class__}, descrição: {error}. ')
    else:
        print(f'Ganhando R$ {ganho_por_hora:.2f} por hora, trabalhando {trabalha_horas_por_dia} horas por dias', end=' ')
        print(f'{trabalha_dias_por_semana} dias por semana, ao final do mês seu salário é de R$ {calculo_salario_mes:.2f} por mês. ')
        break
