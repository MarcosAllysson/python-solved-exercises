"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno
programa que teste sua classe.

Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o
salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, porcentual):
        if porcentual > 0:
            self.salario += self.salario * porcentual
        else:
            return 'Aumento de no mínimo 1%'


class Empresa(Funcionario):
    def __init__(self, nome, salario, empresa):
        super().__init__(nome, salario)
        self.empresa = empresa

    def getEmpresa(self):
        return self.empresa

    def resumoFuncionario(self):
        return f'DADOS DO FUNCIONÁRIO:' \
               f'\nNome: {self.getNome()}' \
               f'\nSalário: ${self.getSalario():.2f}' \
               f'\nEmpresa: {self.getEmpresa()}'


for funcionario in range(1, 11):
    f = Empresa(f'Funcionário {funcionario}', funcionario*funcionario, 'Reino de Deus')
    f.aumentarSalario(funcionario + 1)
    print(f'{f.resumoFuncionario()}')
    print()
