"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
from time import sleep


try:
    asks = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    answers = list()

    for ask in range(5):
        while True:
            ask_temp = str(input(f"\n{ask+1}° pergunta: " + asks[ask] + '\nSim ou não? -> ')).strip().upper()[0]
            if ask_temp in 'SN':
                answers.append(ask_temp)
                break
            print('\n \033[31mResponda somente Sim ou Não!\033[m')

except Exception as error:
    print(error)

else:
    print('\n \033[36mANALISANDO RESPOSTAS...\033[m')
    sleep(2)
    positive_answer = 0

    for answer in answers:
        if answer == 'S':
            positive_answer += 1

    print('Classificação: ', end='')
    if positive_answer == 2:
        print('Suspeita')
    elif positive_answer == 3 or positive_answer == 4:
        print('Cúmplice')
    elif positive_answer == 5:
        print('Assassino')
    else:
        print('Inocente')

finally:
    print('\n \033[m por hoje é isso, aguarde possível contato!\033[m'.title())
