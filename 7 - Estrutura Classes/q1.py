"""
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor


bola = Bola('amarelo', 3.4, 'plástico')
print(bola.mostraCor())

bola.trocaCor('preta')
print(bola.mostraCor())
