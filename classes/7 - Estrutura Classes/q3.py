"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve
criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarAltura(self, altura):
        self.altura = altura

    def mudarBase(self, base):
        self.base = base

    def getAltura(self):
        return self.altura

    def getBase(self):
        return self.base

    def calculaArea(self):
        return self.base * self.altura

    def calculaPerimetro(self):
        return self.base * 2 + self.altura * 2


try:
    while True:
        base = float(input('Informe a base: '))
        altura = float(input('Altura: '))

        if base > 0 and altura > 0:
            # Criando objeto
            retangulo = Retangulo(base, altura)

            # Printando e calculando perímetro / área
            print(f'Área: {retangulo.calculaArea():.2f}m')
            print(f'Perímetro: {retangulo.calculaPerimetro():.2f}m')

            # Finalizando programa.
            break

        print('Base e altura devem ser maiores que 0.')

except:
    print('Erro, tente novamente...')


