"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""


def fibo(num):
    primeiro_termo = 0
    segundo_termo = 1
    fibo = []

    for i in range(num):
        terceiro_termo = primeiro_termo + segundo_termo
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        fibo.append(segundo_termo)

    return f'{num} termos de Fibonacci: {fibo}.'


while True:
    try:
        termo = int(input('Quer gerar quantos termos de Fibonacci? '))
        if termo > 0:
            print(fibo(termo))
            break
        print('\nMínimo valor: 1')

    except Exception as e:
        print(f'\nErro {e}, tente novamente...')
