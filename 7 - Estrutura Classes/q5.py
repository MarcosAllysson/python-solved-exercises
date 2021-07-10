"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = str(numero_conta)
        self.nome_correntista = str(nome_correntista)
        self.saldo = float(saldo)

    def alterarNome(self, nome):
        if str(nome).isalpha() and len(nome) > 2:
            self.nome_correntista = nome
            print(f'Nome alterado com sucesso para: {self.nome_correntista}')
        else:
            print('Não foi possível alterar o nome.')

    def deposito(self, quantia):
        if quantia > 1:
            self.saldo += quantia
            print(f'Depósito feito com sucesso.\nNovo saldo: ${self.saldo:.2f}')

    def saque(self, quantia):
        if 0 < quantia < self.saldo:
            self.saldo -= quantia
            print(f'Saque efetuado com sucesso.\nNovo saldo: ${self.saldo:.2f}')
        else:
            print('Não foi possível efetuar o saque.')

    def getSaldo(self):
        return self.saldo

    def __str__(self):
        return f'Nome: {self.nome_correntista}' \
               f'\nConta: {self.nome_correntista}' \
               f'\nSaldo: ${self.getSaldo():.2f}'


cc = ContaCorrente('123.321', 'Silva')
cc.deposito(3)
cc.saque(2)
print(cc)
