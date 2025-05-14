lojas = []

def criar_loja():
    nome = input("Nome da loja: ")
    localizacao = input("Localização: ")
    loja = {
        "id": len(lojas) + 1,
        "nome": nome,
        "localizacao": localizacao
    }
    lojas.append(loja)
    print("Loja cadastrada com sucesso!")

def listar_lojas():
    if not lojas:
        print("Nenhuma loja cadastrada.")
        return
    print("\n--- Lista de Lojas ---")
    for loja in lojas:
        print(f"ID: {loja['id']}, Nome: {loja['nome']}, Localização: {loja['localizacao']}")

def editar_loja():
    nome = input("Digite o nome da loja a ser editada: ")
    for loja in lojas:
        if loja['nome'] == nome:
            nova_localizacao = input("Nova localização: ")
            loja['localizacao'] = nova_localizacao
            print("Loja atualizada com sucesso!")
            return
    print("Loja não encontrada.")

def excluir_loja():
    nome = input("Digite o nome da loja a ser excluída: ")
    for loja in lojas:
        if loja['nome'] == nome:
            lojas.remove(loja)
            print("Loja excluída com sucesso!")
            return
    print("Loja não encontrada.")
