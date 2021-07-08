"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudarValorLado(self, valor):
        self.tamanho_do_lado = valor

    def getValorLado(self):
        return self.tamanho_do_lado

    def calculaArea(self):
        return self.tamanho_do_lado * self.tamanho_do_lado


quadrado = Quadrado(5)
print(f'Lado do quadrado: {quadrado.getValorLado()}')

quadrado.mudarValorLado(6)
print(f'Novo lado: {quadrado.getValorLado()}')

print(f'Área do quadrado: {quadrado.calculaArea()}m')
