"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
"""


class LojaDeConveniencia:
    def __init__(self, lista_precos_produto):
        self.lista_precos_produto = lista_precos_produto
        self.total_compra = 0
        self.pagamento_cliente = 0

    def getValorProdutos(self):
        for produto, valor in enumerate(self.lista_precos_produto):
            print(f'Produto {produto+1}: R$ {valor:.2f}')

    def totalCompra(self):
        self.total_compra = sum(self.lista_precos_produto)
        return self.total_compra

    def valorTroco(self, valor_cliente):
        self.pagamento_cliente = valor_cliente
        troco = self.pagamento_cliente - self.totalCompra()
        return troco

    def notaFiscal(self):
        print('\n \033[1;36m LOJAS TABAJARA: \033[m')
        self.getValorProdutos()
        print(f'Total: R$ {self.totalCompra():.2f}')
        print(f'Dinheiro: R$ {self.pagamento_cliente:.2f}')
        print(f'Troco: R$ {self.valorTroco(self.pagamento_cliente):.2f}')


# programa principal
while True:
    try:
        while True:
            precos = list()

            while True:
                preco = float(input('Informe o valor do produto ou 0 para finalizar a compra: R$ '))
                if preco == 0:
                    break
                elif preco >= 1:
                    precos.append(preco)
                else:
                    print('\033[31mApenas valores superior a R$ 1 ou informe 0 para finalizar a compra.\033[m')

            # instanciando objeto da classe e printando valor da compra
            compra_cliente = LojaDeConveniencia(precos)
            print(f'\nTotal compra: R$ {compra_cliente.totalCompra():.2f}')

            # pegando valor em dinheiro do cliente verificando se é maior que o total da compra
            while True:
                valor = float(input('Informe valor em dinheiro pra finalizar sua compra: R$ '))
                if valor >= compra_cliente.totalCompra():
                    compra_cliente.valorTroco(valor)
                    break
                print('\n \033[31mNão é possível finalizar compra, informe valor igual ou superior ao total da compra.')

            # printando nota fiscal
            compra_cliente.notaFiscal()

            # perguntando se quer continuar
            proxima_compra = str(input('\nQuer processar outra compra? (Sim/Não): ')).strip().upper()[0]
            if proxima_compra == 'N':
                print('\n \033[36mOk, saindo. Até logo! \033[m')
                break

    except Exception as e:
        print(f'{e}')

    else:
        break
