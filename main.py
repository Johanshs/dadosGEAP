class Dependente:
    def __init__(self, nome, cpf, data_nascimento, parentesco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.parentesco = parentesco

    def __repr__(self):
        return f"Dependente({self.nome}, {self.cpf}, {self.data_nascimento}, {self.parentesco})"


class Titular:
    def __init__(self, nome, cpf, matricula, data_nascimento, dependentes=None):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.dependentes = dependentes if dependentes else []

    def adicionar_dependente(self, dependente):
        self.dependentes.append(dependente)

    def __repr__(self):
        return f"Titular({self.nome}, {self.cpf}, {self.matricula}, {self.data_nascimento}, Dependentes: {len(self.dependentes)})"
