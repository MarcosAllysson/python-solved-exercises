from time import sleep

"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""


def crime(lista_resposta):
    resp_positiva = []

    #  analisando quantidade de respostas positivas
    for resposta in lista_resposta:
        if resposta == 'S':
            resp_positiva.append(resposta)

    #  checagem pra enquadramento no caso
    if len(resp_positiva) == 2:
        msg = 'Suspeita...'
    elif len(resp_positiva) == 3 or len(resp_positiva) == 4:
        msg = 'Cúmplice...'
    elif len(resp_positiva) == 5:
        msg = 'Só 1 segundo, vou falar com um colega e já te respondo. AGUARDE EM CASA!'
    else:
        msg = 'Inocente, pode ir pra casa. Qualquer coisa entro em contato! '

    return f'\033[1;33m{msg}\033[m'


while True:
    try:
        perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]

        list_resposta = list()

        for i in range(5):
            print(f'\n \033[36m{i+1}° pergunta: {perguntas[i]}\033[m', end=' ')

            while True:
                resposta = str(input('Sim ou Não? ')).strip().upper()[0]
                if resposta in 'SN':
                    list_resposta.append(resposta)
                    break
                print('\n \033[31mResposta inválida! Responda com sim ou não somente!\033[m')

        print('\n \033[32mOk, verificando fatos do crime...\033[m')
        sleep(3)

    except:
        print('Erro! Tente de novo...')

    else:
        print(crime(list_resposta))
        break
