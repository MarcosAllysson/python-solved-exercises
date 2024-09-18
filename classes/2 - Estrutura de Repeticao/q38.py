from datetime import date
"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário.
"""
# Ano atual
ano_atual = date.today().year


def aumento_salarial(ano_usuario, salario_usuario):
    salario = salario_usuario
    percentual = 1.5 / 100
    novo_salario = salario + percentual * salario

    while ano_usuario <= ano_atual:
        novo_percentual = percentual * 2
        novo_salario += novo_percentual * novo_salario
        ano_usuario += 1

    return f'\n \033[36mNovo salário atual em {ano_atual}, é de:\033[m R$ {novo_salario:.2f}'


# Programa principal
while True:
    try:
        while True:
            ano = int(input('Informe o ano de entrada: '))
            sal = float(input('Informe o salário: R$ '))
            if 1900 <= ano <= ano_atual and sal >= 1:
                print(aumento_salarial(1997, sal))
                break
            print(f'\n \033[31mErro: ano mínimo permitido 1900 até ano atual e salário superior a R$ 1.\033[m')

        # saindo do loop
        break
    except:
        print('\033[31mTente novamente, pois houve algum erro...\033[m')
