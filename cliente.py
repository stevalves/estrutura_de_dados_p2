clientes = [
    {"id": 1, "nome": "Ana Souza", "email": "ana.souza@gmail.com"},
    {"id": 2, "nome": "Bruno Lima", "email": "bruno.lima@hotmail.com"},
    {"id": 3, "nome": "Carla Mendes", "email": "carla.mendes@yahoo.com"},
]
emails_cadastrados = set()
emails_cadastrados.add("ana.souza@gmail.com")
emails_cadastrados.add("bruno.lima@hotmail.com")
emails_cadastrados.add("carla.mendes@yahoo.com")

id_cliente = 1 + len(clientes)


def criar_cliente():
    global id_cliente
    nome = input("Nome: ")
    email = input("Email: ")

    if email in emails_cadastrados:
        print("Email já cadastrado!")
        return

    cliente = {
        "id": id_cliente,
        "nome": nome,
        "email": email,
    }
    clientes.append(cliente)
    emails_cadastrados.add(email)
    id_cliente += 1
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- Lista de Clientes ---")
    for cliente in clientes:
        print(
            f"ID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}"
        )


def editar_cliente():
    id_cliente = int(input("Digite o id do cliente a ser editado: "))
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            novo_nome = input("Novo nome (pressione Enter para manter): ")
            novo_email = input("Novo email (pressione Enter para manter): ")
            if novo_email in emails_cadastrados and novo_email != cliente["email"]:
                print("Email já cadastrado!")
                return
            if novo_email:
                emails_cadastrados.discard(cliente["email"])
                cliente["email"] = novo_email
                emails_cadastrados.add(novo_email)
            if novo_nome:
                cliente["nome"] = novo_nome
            print("Cliente atualizado com sucesso!")
            return
    print("Cliente não encontrado.")


def excluir_cliente():
    id_cliente = int(input("Digite o id do cliente a ser excluído: "))
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            clientes.remove(cliente)
            emails_cadastrados.remove(cliente["email"])
            print("Cliente excluído com sucesso!")
            return
    print("Cliente não encontrado.")


def pegar_cliente_por_id(id):
    for cliente in clientes:
        if cliente["id"] == id:
            return cliente
    return None
