class CadastroPessoa: #Questão 1
    def __init__(self, nome, instituicao, cpf):
        self.nome = nome
        self.instituicao = instituicao
        self.cpf = cpf

    def resumo(self): #Questão 2
        return print(
f"""Bem-vindo(a), {self.nome}!
Instituição: {self.instituicao}
""")
    
    def __str__(self): #Questão 2
        print(f"""
Nome: {self.nome}
Instituição: {self.instituicao}
Cpf: {self.cpf}
            """)

class CadastroSala: #Questão 1
    def __init__(self, nome_sala, local, capacidade):
        self.nome_sala = nome_sala
        self.local = local
        self.capacidade = capacidade

    def resumo(self): #Questão 2
        return print(f"""
Nome da sala: {self.nome_sala}
Local: {self.local}
""")
            
    def __str__(self): #Questão 2
            print(f"""
Sala: {self.nome_sala}
Local: {self.local}
Capacidade: {self.capacidade}
                """)


class AgendamentoSala: #Questão 1
    def __init__(self):
        self.FazerAgendamento = [] #Questão 3

    def adicionar_agendamento(self): #Questão 2
            self.FazerAgendamento.append("Gabriel Morais")
            self.FazerAgendamento.append("Sala 1")
            print(f"Agendamento realizado!")
            
    def listar_agendamentos(self): #Questão 2
        if not self.FazerAgendamento:
            print("Você não possui nenhum agendamento!")
        else:
            print(f"Seus agendamentos: {self.FazerAgendamento}")

    def buscar_agendamento(self): #Questão 3
        sala_agendamento = input("Gostaria de filtrar seus agendamentos pra qual sala? ")
        if sala_agendamento not in self.FazerAgendamento:
            print("Não foi encontrado agendamentos nessa sala.")
        else:
            for sala_agendamento in sala(self.FazerAgendamento):
                print(f"{self.FazerAgendamento[pessoa]}")

    def buscar_agendamento_pessoas(self): #Questão 3
        pessoa_agendamento = input("Gostaria de filtrar os agendamentos por qual nome? ")
        if pessoa_agendamento not in self.FazerAgendamento:
            print("Não foi possivel encontrar agendamentos nesse nome.")
        else:
            for pessoa_agendamento in (self.FazerAgendamento):
                print(f"{self.FazerAgendamento[sala]}")
         

pessoa = CadastroPessoa("Gabriel", "Univassouras", 12345678)
pessoa.resumo()
pessoa.__str__()
sala = CadastroSala("Sala 1", "Primeiro andar", "70 pessoas")
sala.resumo()
sala.__str__()
agendar = AgendamentoSala()
agendar.adicionar_agendamento()
agendar.listar_agendamentos()
agendar.buscar_agendamento()
agendar.buscar_agendamento_pessoas()