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

# criar um método que apresente esse humano

ser1 = Humano('Gabriel', 25, '1.75', 'Onívoro', '12345678900', 'Masculino')

print(ser1.nome)