def numeros_primos(numero):
    """
    Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
    O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
    Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
    """
    cont_div = 0
    primos = list()

    for i in range(1, numero + 1):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
                cont_div += 1

        if div == 2:
            primos.append(i)

    print(f"\nTodos os primos de 1 a {numero}: {primos}"
          f"\nNúmero de divisões: {cont_div}")


while True:
    try:
        numero = int(input('Informe um número inteiro: '))

    except Exception as erro:
        print(f'{erro}')

    else:
        numeros_primos(numero)

        break


