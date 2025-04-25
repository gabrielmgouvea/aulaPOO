class ser_vivo:
    def __init__(self, genero, alimentacao, altura):
        self.genero = genero
        self.alimentacao = alimentacao
        self.altura = altura


# sub class
class Humano(ser_vivo):
    def __init__(self, nome, idade, altura, alimentacao, cpf, genero):
        super().__init__(genero, alimentacao, altura)
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class estudantes(Humano):
    def __init__(self, nome, idade, altura, alimentacao, cpf, genero, curso):
        super().__init__(nome, idade, altura, alimentacao, cpf, genero)
        self.curso = curso


# criar um método que apresente esse humano
# criar uma classe estudantes que faça herança da classe humano
# atributo curso
ser1 = estudantes('Gabriel', 25, '1.75', 'Onívoro', '12345678900', 'Masculino', 'software')

print(ser1.nome)
