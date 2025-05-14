clientes = []
emails_cadastrados = set()

def criar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")

    if email in emails_cadastrados:
        print("Email já cadastrado!")
        return

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "email": email,
    }
    clientes.append(cliente)
    emails_cadastrados.add(email)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- Lista de Clientes ---")
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}")

def editar_cliente():
    id = input("Digite o id do cliente a ser editado: ")
    for cliente in clientes:
        if cliente['id'] == id:
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            if novo_email in emails_cadastrados and novo_email != cliente['email']:
                print("Email já cadastrado!")
                return
            emails_cadastrados.discard(cliente['email'])
            cliente['email'] = novo_email
            emails_cadastrados.add(novo_email)
            cliente['nome'] = novo_nome
            print("Cliente atualizado com sucesso!")
            return
    print("Cliente não encontrado.")

def excluir_cliente():
    id = input("Digite o id do cliente a ser excluído: ")
    for cliente in clientes:
        if cliente['id'] == id:
            clientes.remove(cliente)
            emails_cadastrados.remove(cliente['email'])
            print("Cliente excluído com sucesso!")
            return
    print("Cliente não encontrado.")