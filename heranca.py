class Pessoa:
    # A __init__() é chamada automaticamente
    # toda vez que a classe está sendo usada
    # para criar um novo objeto.
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def __get__(self):
        print(self.nome, self.idade)


pessoa = Pessoa('Tupi', 19)
pessoa.__get__()


class Estudante(Pessoa):
    def __init__(self, nome='', idade=0, sala=0, nota_total=0.0):
        self.sala = sala
        self.nota_total = nota_total
        super().__init__(nome, idade)

    def __get__(self):
        print(self.nome, self.idade, self.sala, self.nota_total)


estudante = Estudante('Carlos', 15, 10, 15.95)
estudante.__get__()
