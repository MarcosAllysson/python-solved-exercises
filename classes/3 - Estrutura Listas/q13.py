"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar
o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

try:
    temp_months = list()
    list_months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Semptember', 'October', 'November', 'December'
    ]

    for month in range(12):
        temp_months.append(float(input(f'Temperature of {list_months[month]}: ')))

    # average
    temp_months_avg = sum(temp_months) / len(temp_months)
    print(f'\n - Average temperature: {temp_months_avg:.2f}°')

    # showing months wich temps were higher than the average
    for key, temp in enumerate(temp_months):
        if temp > temp_months_avg:
            print(f'Month {key+1} - {list_months[key]}, temperature {temp:.2f}° was higher than the average.')

except Exception as error:
    print(error)
