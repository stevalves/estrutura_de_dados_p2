lojas = [
    {
        "id": 1,
        "nome": "Supermercado Pão de Açúcar",
        "localizacao": "Av. Paulista, 900 - São Paulo",
    },
    {
        "id": 2,
        "nome": "Carrefour Hipermercado",
        "localizacao": "Rua Domingos de Morais, 2564 - São Paulo",
    },
    {
        "id": 3,
        "nome": "Extra Supermercado",
        "localizacao": "Av. Brigadeiro Faria Lima, 2232 - São Paulo",
    },
    {
        "id": 4,
        "nome": "Assaí Atacadista",
        "localizacao": "Av. Jacu-Pêssego, 5100 - São Paulo",
    },
    {
        "id": 5,
        "nome": "Dia Supermercado",
        "localizacao": "Rua Augusta, 1500 - São Paulo",
    },
]
id_loja = 1 + len(lojas)


def criar_loja():
    global id_loja
    nome = input("Nome da loja: ")
    localizacao = input("Localização: ")
    loja = {"id": len(lojas) + 1, "nome": nome, "localizacao": localizacao}
    lojas.append(loja)
    id_loja += 1
    print("Loja cadastrada com sucesso!")


def listar_lojas():
    if not lojas:
        print("Nenhuma loja cadastrada.")
        return
    print("\n--- Lista de Lojas ---")
    for loja in lojas:
        print(
            f"ID: {loja['id']}, Nome: {loja['nome']}, Localização: {loja['localizacao']}"
        )


def editar_loja():
    id_loja = int(input("Digite o id da loja a ser editada: "))
    for loja in lojas:
        if loja["id"] == id_loja:
            novo_nome = input("Novo nome (deixe vazio para não alterar): ")
            nova_localizacao = input(
                "Nova localização (deixe vazio para não alterar): "
            )
            if novo_nome:
                loja["nome"] = novo_nome
            if nova_localizacao:
                loja["localizacao"] = nova_localizacao
            print("Loja atualizada com sucesso!")
            return
    print("Loja não encontrada.")


def excluir_loja():
    id_loja = int(input("Digite o id da loja a ser excluída: "))
    for loja in lojas:
        if loja["id"] == id_loja:
            lojas.remove(loja)
            print("Loja excluída com sucesso!")
            return
    print("Loja não encontrada.")


def pegar_loja_por_id(id_loja):
    for loja in lojas:
        if loja["id"] == id_loja:
            return loja
    return None
