"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""


def any_values(*args):
    print(f'- Quantity: {len(args[0])}')
    print(f'- Values: {args[0]}')
    # for value in args[0]:
    #     print(value, end='')

    print('\n- Inverted: ')
    for value in args[0][::-1]:
        print(value)

    print(f'- Sum: {sum(args[0])}')
    average = sum(args[0]) / len(args[0])
    print(f'- Average: {average:.2f}')

    above_average_quantity = 0
    for value in args[0]:
        if value > average:
            above_average_quantity += 1
    print(f'- Above the average: {above_average_quantity}')

    below_seven = 0
    for value in args[0]:
        if value < 7:
            below_seven += 1
    print(f'- Numbers below 7: {below_seven}.')


try:
    values = list()

    while True:
        value = int(input('Insert value OR 1 to stop: '))
        if value == 1:
            print('\n \033[36mOk, lets take a look at the number now. See you soon :D\033[m')
            break
        else:
            values.append(value)

    any_values(values)


except Exception as error:
    print(error)
