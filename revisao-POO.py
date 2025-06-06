# Classe que representa uma conta bancária
class Conta:
    def __init__(self, nome_cliente, numero_conta, agencia, senha, saldo_inicial=0.0):
        # Atributos conforme o diagrama
        self.__nome_cliente = nome_cliente
        self.__numero_conta = numero_conta
        self.__agencia = agencia
        self.__saldo = saldo_inicial
        self.__limite_cheque_especial = 1000.0  # Valor padrão
        self.__limite_cartao = 2000.0          # Valor padrão
        self.__pix = None
        self.__senha = senha

    # Métodos para acessar dados privados de forma segura (Getters)
    def get_saldo(self):
        return self.__saldo

    def get_nome_cliente(self):
        return self.__nome_cliente

    # Método de autenticação
    def autenticar(self, senha):
        return self.__senha == senha

    # Método para cadastrar uma chave Pix
    def cadastrar_pix(self, chave_pix):
        self.__pix = chave_pix
        print(f"Chave Pix '{chave_pix}' cadastrada para {self.get_nome_cliente()}.")

    # Método para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.get_saldo():.2f}")
        else:
            print("Valor de depósito inválido.")

    # Método para pagar com débito
    def debito(self, valor):
        if self.get_saldo() >= valor:
            self.__saldo -= valor
            return True
        else:
            return False
            
    # Os métodos 'cadastrar', 'pix', 'cheque_especial' e 'cartao_credito' não foram
    # implementados para manter o exemplo focado, mas aqui seria o local deles.

# Classe base para uma loja
class Loja:
    def __init__(self):
        # O catálogo é um dicionário para guardar produto:preço
        self._catalogo = {}

    def adicionar_produto(self, produto, valor):
        self._catalogo[produto] = valor
        print(f"Produto '{produto}' adicionado ao catálogo por R${valor:.2f}.")

    def remover_produto(self, produto):
        if produto in self._catalogo:
            del self._catalogo[produto]
            print(f"Produto '{produto}' removido do catálogo.")
        else:
            print("Produto não encontrado no catálogo.")

    def listar_produtos(self):
        print("\n--- Catálogo da Loja ---")
        if not self._catalogo:
            print("Catálogo vazio.")
        for produto, valor in self._catalogo.items():
            print(f"- {produto}: R${valor:.2f}")
        print("------------------------")

    # Método genérico a ser sobrescrito
    def realizar_venda(self):
        print("Método de venda genérico da loja.")

    # Método genérico a ser sobrescrito
    def oferecer_promocao(self):
        print("Promoção genérica.")


# Loja física que herda de Loja
class LojaFisica(Loja):
    def __init__(self):
        super().__init__()
        self._desconto = 0.0  # Desconto começa em 0%

    def oferecer_promocao(self, desconto_percentual):
        # Recebe o desconto como uma porcentagem (ex: 10 para 10%)
        self._desconto = desconto_percentual / 100.0
        print(f"\n*** PROMOÇÃO ATIVADA: {desconto_percentual}% de desconto em todos os produtos! ***")

    def realizar_venda(self, produto, conta_cliente, senha):
        print(f"\nTentando vender '{produto}' para {conta_cliente.get_nome_cliente()}...")
        # 1. Autenticar o cliente
        if not conta_cliente.autenticar(senha):
            print("Falha na venda: Senha incorreta.")
            return

        # 2. Verificar se o produto existe
        if produto not in self._catalogo:
            print(f"Falha na venda: Produto '{produto}' não existe.")
            return

        # 3. Calcular o preço final com desconto
        preco_original = self._catalogo[produto]
        preco_final = preco_original * (1 - self._desconto)
        print(f"Preço original: R${preco_original:.2f}. Preço com desconto: R${preco_final:.2f}")

        # 4. Tentar o pagamento via débito
        if conta_cliente.debito(preco_final):
            print(f"Venda de '{produto}' para {conta_cliente.get_nome_cliente()} realizada com sucesso!")
            print(f"Saldo restante na conta: R${conta_cliente.get_saldo():.2f}")
        else:
            print("Falha na venda: Saldo insuficiente.")

# --- Demonstração de Uso ---

# Criação de uma conta para um cliente
conta_bruno = Conta("Bruno", "12345-6", "001", "senha123", 1000.0)

# Criação de uma loja física
loja_centro = LojaFisica()

# Adicionando produtos à loja
loja_centro.adicionar_produto("Camisa", 80.0)
loja_centro.adicionar_produto("Calça Jeans", 150.0)
loja_centro.adicionar_produto("Tênis", 220.0)

# Mostrando o catálogo
loja_centro.listar_produtos()

# A loja inicia uma promoção
loja_centro.oferecer_promocao(20) # 20% de desconto

# Bruno tenta comprar uma calça
loja_centro.realizar_venda("Calça Jeans", conta_bruno, "senha123")

# Bruno tenta comprar um tênis com a senha errada
loja_centro.realizar_venda("Tênis", conta_bruno, "senha_errada")

loja_centro.realizar_venda("Camisa", conta_bruno, "senha123")