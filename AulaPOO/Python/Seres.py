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

class Estudante(Humano):
    def __init__(self, nome, idade, altura, alimentacao, cpf, genero, curso=None):
        super().__init__(nome, idade, altura, alimentacao, cpf, genero)
        self.curso = curso

    def __str__(self): #Questão 2
            print(f"""
Nome: {self.nome}
Idade: {self.idade}
Altura: {self.altura}
Alimentação: {self.alimentacao}
CPF: {self.cpf}
Gênero: {self.genero}
Curso: {self.curso}
                """)

# criar um método que apresente esse humano
# criar uma classe estudantes que faça herança da classe humano
# atributo curso

ser1 = Estudante('João Gabriel', 25, '1.75', 'Onívoro', '12345678900', 'Masculino', 'Engenharia de Software')
ser1.__str__()

print(ser1.nome)
