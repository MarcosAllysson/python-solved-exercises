"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""


while True:
    phone = str(input('Digite o telefone: ')).strip()

    if 7 <= len(phone) <= 9:
        # Tratando telefone COM traço
        if '-' in phone:
            break_phone = phone.split('-')

            if break_phone[0].isdigit() and break_phone[1].isdigit():
                # Telefone com 7 dígitos. Exemplo: (461-0133)
                if len(phone) - 1 == 7:
                    formated_number = str('3' + phone)
                    print(f'Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.'
                          f'\nTelefone corrigido com formatação: {formated_number}')
                    break

                # Telefone com 8 dígitos. Exemplo: (3461-0133)
                if len(phone) - 1 == 8:
                    print(f'Telefone digitado corretamente e não precisa de formatação: {phone}')
                    break

            else:
                print('Telefone Inválido!')
                break

        # Tratando telefone SEM traço
        if phone.isdigit():

            # Telefone com 7 dígitos. Exemplo: (4610133)
            if len(phone) == 7:
                formated_number = str('3' + phone[:3] + '-' + phone[3:])
                print(f'Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.'
                      f'\nTelefone corrigido com formatação: {formated_number}')
                break

            # Telefone com 8 dígitos. Exemplo: (34610133)
            if len(phone) == 8:
                formated_number = str(phone[:4] + '-' + phone[4:])
                print(f'Telefone corrigido com formatação: {formated_number}')
                break

        # Se tiver tamanho esperado, mas não tem traço e nem é dígito. Inválido!
        else:
            print('Telefone Inválido!')
            break

    # Telefone inválido.
    print('\nTelefone Inválido!')
