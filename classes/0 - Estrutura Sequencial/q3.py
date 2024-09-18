"""
Faça um Programa que peça dois números e imprima a soma.
"""

while True:
    try:
        primeiro_numero = int(input('Digite 1° número: '))
        segundo_numero = int(input('Digite 2° número: '))
        soma = primeiro_numero + segundo_numero
    except Exception as error:
        print(f'Não consegui somar, erro: Exceção: {error.__class__}, descrição: {error} ')
    else:
        print(f'Soma de {primeiro_numero} + {segundo_numero} = {soma}.')
        break
