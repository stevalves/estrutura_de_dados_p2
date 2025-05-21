from cliente import pegar_cliente_por_id, listar_clientes
from produto import pegar_produto_por_id, listar_produtos


class NoCompra:
    contador_id = 1

    def __init__(self, cliente, produto, quantidade):
        self.dados = {
            "id": NoCompra.contador_id,
            "cliente": cliente,
            "produto": produto,
            "quantidade": quantidade,
        }
        NoCompra.contador_id += 1
        self.proximo = None


class ListaEncadeadaCompras:
    def __init__(self):
        self.inicio = None

    def adicionar_compra(self, cliente, produto, quantidade):
        nova_compra = NoCompra(cliente, produto, quantidade)
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
            cliente = dados["cliente"]
            produto = dados["produto"]
            print(
                f"ID da compra: {dados['id']}, Cliente: {cliente['nome']} ({cliente['email']}), "
                f"Produto: {produto['info'][0]}, Valor unitário: R${produto['info'][1]:.2f}, Quantidade: {dados['quantidade']}, Valor Total: R${(produto['info'][1] * dados['quantidade']):.2f}"
            )
            atual = atual.proximo

    def excluir_compra(self, compra_id):
        atual = self.inicio
        anterior = None
        while atual:
            if atual.dados["id"] == compra_id:
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
    listar_clientes()
    try:
        cliente_id = int(input("Insira o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return

    cliente = pegar_cliente_por_id(cliente_id)
    if not cliente:
        print("Cliente não encontrado.")
        return

    listar_produtos()
    try:
        produto_id = int(input("Insira o ID do produto: "))
    except ValueError:
        print("ID inválido.")
        return

    produto = pegar_produto_por_id(produto_id)
    if not produto:
        print("Produto não encontrado.")
        return
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return
    except ValueError:
        print("Quantidade inválida.")
        return

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
