produtos = []

def criar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    loja = input("Nome da loja responsável: ")
    produto = {
        "id": len(produtos) + 1,
        "info": (nome, preco),
        "loja": loja
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("\n--- Lista de Produtos ---")
    for produto in produtos:
        nome, preco = produto['info']
        print(f"ID: {produto['id']}, Produto: {nome}, Preço: R${preco:.2f}, Loja: {produto['loja']}")

def editar_produto():
    nome_produto = input("Digite o nome do produto a ser editado: ")
    for produto in produtos:
        nome, _ = produto['info']
        if nome == nome_produto:
            novo_nome = input("Novo nome: ")
            novo_preco = float(input("Novo preço: "))
            produto['info'] = (novo_nome, novo_preco)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def excluir_produto():
    nome_produto = input("Digite o nome do produto a ser excluído: ")
    for produto in produtos:
        nome, _ = produto['info']
        if nome == nome_produto:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")