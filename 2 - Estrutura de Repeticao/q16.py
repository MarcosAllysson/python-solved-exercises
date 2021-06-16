"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""


def fibo():
    primeiro_termo = 0
    segundo_termo = 1
    fibo = []

    while True:
        terceiro_termo = primeiro_termo + segundo_termo
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        fibo.append(segundo_termo)

        if segundo_termo > 500:
            break

    return f'Termos de Fibonacci: {fibo}.'


# main
if __name__ == '__main__':
    print(fibo())
