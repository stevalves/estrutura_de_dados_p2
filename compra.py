class NoCompra:
    contador_id = 1

    def __init__(self, cliente_email, produto_nome, quantidade):
        self.dados = {
            "id": NoCompra.contador_id,
            "cliente": cliente_email,
            "produto": produto_nome,
            "quantidade": quantidade
        }
        NoCompra.contador_id += 1
        self.proximo = None

class ListaEncadeadaCompras:
    def __init__(self):
        self.inicio = None

    def adicionar_compra(self, cliente_email, produto_nome, quantidade):
        nova_compra = NoCompra(cliente_email, produto_nome, quantidade)
        if not self.inicio:
            self.inicio = nova_compra
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nova_compra
        print("Compra registrada com sucesso!")

    def listar_compras(self):
        if not self.inicio:
            print("Nenhuma compra registrada.")
            return
        atual = self.inicio
        print("\n--- Lista de Compras ---")
        while atual:
            dados = atual.dados
            print(f"ID: {dados['id']}, Cliente: {dados['cliente']}, Produto: {dados['produto']}, Quantidade: {dados['quantidade']}")
            atual = atual.proximo

    def excluir_compra(self, compra_id):
        atual = self.inicio
        anterior = None
        while atual:
            if atual.dados['id'] == compra_id:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                print("Compra excluída com sucesso!")
                return
            anterior = atual
            atual = atual.proximo
        print("Compra não encontrada.")

    def cancelar_ultima_compra(self):
        if not self.inicio:
            print("Nenhuma compra para cancelar.")
            return
        if not self.inicio.proximo:
            self.inicio = None
            print("Última compra cancelada com sucesso!")
            return
        atual = self.inicio
        while atual.proximo and atual.proximo.proximo:
            atual = atual.proximo
        atual.proximo = None
        print("Última compra cancelada com sucesso!")

compras = ListaEncadeadaCompras()

def criar_compra():
    cliente = input("Email do cliente: ")
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    compras.adicionar_compra(cliente, produto, quantidade)

def listar_compras():
    compras.listar_compras()

def excluir_compra():
    try:
        compra_id = int(input("Digite o ID da compra a excluir: "))
        compras.excluir_compra(compra_id)
    except ValueError:
        print("ID inválido.")

def cancelar_ultima_compra():
    compras.cancelar_ultima_compra()