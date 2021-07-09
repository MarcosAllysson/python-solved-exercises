"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
"""


def verifica_cpf(cpf):
    cpf_valido = False

    if len(cpf) == 14:
        pi3 = cpf[:3]
        pm3 = cpf[4:7]
        pf3 = cpf[8:11]
        ff3 = cpf[12:14]

        if pi3.isdigit() and pm3.isdigit() and pf3.isdigit() and ff3.isdigit():
            if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
                cpf_valido = True

    if cpf_valido:
        return f' - CPF \033[33m{cpf}\033[m é válido'

    return f'CPF \033[31m{cpf} inválido!\033[m'


try:
    cpf_usuario = str(input('Digite CPF: ')).strip()
    print(verifica_cpf(cpf_usuario))

except Exception as e:
    print(e)
