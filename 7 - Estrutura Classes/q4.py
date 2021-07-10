"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, cm):
        self.altura += cm

    def __str__(self):
        return f'\nPESSOA:' \
               f'\nNome: {self.nome}' \
               f'\nIdade: {self.idade} anos' \
               f'\nPeso: {self.peso}kg' \
               f'\nAltura: {self.altura}m'


class Aluno(Pessoa):
    def __init__(self, nome, idade, peso, altura, disciplina, faculdade):
        super().__init__(nome, idade, peso, altura)
        self.disciplina = disciplina
        self.faculdade = faculdade

    def __str__(self):
        return f'\nALUNO:' \
               f'\nNome: {self.nome}' \
               f'\nIdade: {self.idade} anos' \
               f'\nPeso: {self.peso}kg' \
               f'\nAltura: {self.altura}m' \
               f'\nDisciplina: {self.disciplina}' \
               f'\nFaculdade: {self.faculdade}'


person = Pessoa('Dev', 19, 60, 1.74)
print(person)

student = Aluno('Silva', 30, 80, 1.90, 'Cálculo', 'IFB')
print(student)
student.crescer(0.5)
student.emagrecer(2)
student.engordar(9.8)
student.envelhecer(4)
print(student)
