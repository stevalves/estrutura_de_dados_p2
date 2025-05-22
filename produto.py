from loja import pegar_loja_por_id, listar_lojas

produtos = [
    {
        "id": 1,
        "info": ("Arroz Tio João 5kg", 24.90),
        "loja": "Supermercado Pão de Açúcar",
    },
    {"id": 2, "info": ("Leite Italac 1L", 4.75), "loja": "Carrefour Hipermercado"},
    {"id": 3, "info": ("Café Pilão 500g", 16.80), "loja": "Extra Supermercado"},
    {"id": 4, "info": ("Óleo de Soja Soya 900ml", 6.50), "loja": "Assaí Atacadista"},
    {"id": 5, "info": ("Açúcar União 1kg", 3.90), "loja": "Dia Supermercado"},
]
id_produto = 1 + len(produtos)


def criar_produto():
    global id_produto
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    listar_lojas()
    loja_id = int(input("ID da loja responsável: "))
    loja = pegar_loja_por_id(loja_id)
    if not loja:
        print("Loja não encontrada.")
        return
    produto = {"id": len(produtos) + 1, "info": (nome, preco), "loja": loja["nome"]}
    produtos.append(produto)
    id_produto += 1
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("\n--- Lista de Produtos ---")
    for produto in produtos:
        nome, preco = produto["info"]
        print(
            f"ID: {produto['id']}, Produto: {nome}, Preço: R${preco:.2f}, Loja: {produto['loja']}"
        )


def editar_produto():
    id_produto = int(input("Digite o id do produto a ser editado: "))
    for produto in produtos:
        if id_produto == id_produto:
            novo_nome = input("Novo nome (pressione Enter para manter):")
            novo_preco = input("Novo preço (pressione Enter para manter):")
            if novo_nome:
                produto["info"] = (novo_nome, produto["info"][1])
            if novo_preco:
                produto["info"] = (produto["info"][0], float(novo_preco))
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")


def excluir_produto():
    id_produto = int(input("Digite o id do produto a ser excluído: "))
    for produto in produtos:
        if id_produto == id_produto:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")


def pegar_produto_por_id(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return None
