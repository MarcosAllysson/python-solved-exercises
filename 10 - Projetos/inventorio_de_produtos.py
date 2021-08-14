"""
Inventário de produto - Crie um aplicativo que gerencie um inventário de produtos. Crie uma classe de produto que tenha
um preço, ID e quantidade à mão. Em seguida, crie uma classe inventory que rastreie vários produtos e possa somar o
valor do inventário.
"""


class Produto:
    def __init__(self, id, preco, quantidade):
        self.id = id
        self.preco = preco
        self.quantidade = quantidade

    def get_id(self):
        return self.id

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade

    def set_id(self, id):
        if id > 1:
            self.id = id
        else:
            print('ID deve ser maior que 1!')

    def set_preco(self, preco):
        if preco > 1:
            self.preco = preco
        else:
            print('Preço deve ser maior que 1!')

    def set_quantidade(self, quantidade):
        if quantidade > 1:
            self.preco = quantidade
        else:
            print('Quantidade deve ser maior que 1!')

    def somar_preco_produto(self):
        return f'{self.preco * self.quantidade:.2f}'


try:
    while True:
        produto_quantidade = int(input('Quer criar quantos produtos? '))
        if 1 <= produto_quantidade:
            break
        print(f'\033[31mErro! No mínimo 1 produto. \033[m')

    for produto in range(produto_quantidade):
        produtos = list()

        for p in range(1):
            produto_temp = list()
            produto_id = p + 1
            produto_preco = float(input(f'Qual valor do produto {produto + 1}? '))
            produto_quantidade = int(input('Quantidade? '))
            print()

            produto_temp.append(produto_id)
            produto_temp.append(produto_preco)
            produto_temp.append(produto_quantidade)

            produtos.append(produto_temp[:])
            # produto_temp.clear()

        print(produtos)

except Exception as error:
    print(f'{error}')
