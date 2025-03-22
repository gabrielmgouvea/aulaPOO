class Pessoa:
    def __init__(self, nome, cpf, altura, idade, profissao, salario):
        self.nome = nome
        self.__cpf = cpf
        self.altura = altura
        self.idade = idade
        self.profissao = profissao
        self.__salario = salario

    def mostrar_cpf(self):
        return self.__cpf
    
    def mostrar_salario(self):
        return self.__salario
    
    def habilidade(self):
        pass

pessoa1 = Pessoa("Zé das Coves", "123.456.789-00", 1.80, 29, "Desenvolvedor", 9000.00)

cpf = pessoa1.mostrar_cpf()

pessoa1.habilidade()

#print(f"{cpf[:4]}......{cpf[7:]}")


print(
    f"""
A pessoa cadastrada é {pessoa1.nome}
Seu cpf é {cpf[:4]}...{cpf[8:]}
de altura {pessoa1.altura}
Sua profissão é {pessoa1.profissao}
e ganha R${pessoa1.mostrar_salario()}
    """
)