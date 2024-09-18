"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
"""


class TV:
    def __init__(self, canal=1, volume=50):
        self.canal = int(canal)
        self.volume = int(volume)

    def getCanal(self):
        print(f'Você está no canal: {self.canal}')

    def setCanal(self, canal):
        if 0 < canal <= 100:
            self.canal = canal
            print(f'Canal atual: {self.canal}')

        else:
            print('Não foi possível mudar de canal.')

    def getVolume(self):
        print(f'Volume: {self.volume}')

    def aumentarVolume(self, volume):
        if 1 <= volume <= 100:
            if volume + self.volume <= 100:
                self.volume += volume
                self.getVolume()

            else:
                print('Volume máximo: 100')

        else:
            print('Não foi possível aumentar o volume.')

    def diminuirVolume(self, volume):
        if 1 <= volume <= 100:
            if self.volume + volume >= 0:
                self.volume -= volume
                self.getVolume()

            else:
                print('Volume mínimo: 0')

        else:
            print('Não foi possível diminuir o volume.')

    def __str__(self):
        return f'\n=================' \
               f'\n \t\tTV' \
               f'\nCanal :  \t{self.canal}' \
               f'\nVolume: \t{self.volume}' \
               f'\n================='


tv = TV()
# print(tv)
tv.getVolume()
tv.getCanal()
tv.setCanal(100)
tv.aumentarVolume(50)
tv.diminuirVolume(78)
print(tv)
