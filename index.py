from cliente import criar_cliente, listar_clientes, editar_cliente, excluir_cliente
from loja import criar_loja, listar_lojas, editar_loja, excluir_loja
from produto import criar_produto, listar_produtos, editar_produto, excluir_produto
from compra import criar_compra, listar_compras, cancelar_ultima_compra

mensagens = {
    "menu_principal": """
===== Menu Principal =====
1. Opções Clientes
2. Opções Lojas
3. Opções Produtos
4. Opções Compras
0. Sair
""",
    "menu_clientes": """
--- Menu Clientes ---
1. Criar Cliente
2. Listar Clientes
3. Editar Cliente
4. Excluir Cliente
0. Voltar
""",
    "menu_lojas": """
--- Menu Lojas ---
1. Criar Loja
2. Listar Lojas
3. Editar Loja
4. Excluir Loja
0. Voltar
""",
    "menu_produtos": """
--- Menu Produtos ---
1. Criar Produto
2. Listar Produtos
3. Editar Produto
4. Excluir Produto
0. Voltar
""",
    "menu_compras": """
--- Menu Compras ---
1. Criar Compra
2. Listar Compras
3. Cancelar Última Compra
0. Voltar
""",
    "opcao_invalida": "Opção inválida. Tente novamente."
}

def menu():
    while True:
        print(mensagens["menu_principal"])
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                while True:
                    print(mensagens["menu_clientes"])
                    opcao_cliente = input("Escolha uma opção: ")

                    match opcao_cliente:
                        case '1': criar_cliente()
                        case '2': listar_clientes()
                        case '3': editar_cliente()
                        case '4': excluir_cliente()
                        case '0': break
                        case _: print(mensagens["opcao_invalida"])
            case '2':
                while True:
                    print(mensagens["menu_lojas"])
                    opcao_loja = input("Escolha uma opção: ")

                    match opcao_loja:
                        case '1': criar_loja()
                        case '2': listar_lojas()
                        case '3': editar_loja()
                        case '4': excluir_loja()
                        case '0': break
                        case _: print(mensagens["opcao_invalida"])
            case '3':
                while True:
                    print(mensagens["menu_produtos"])
                    opcao_produto = input("Escolha uma opção: ")

                    match opcao_produto:
                        case '1': criar_produto()
                        case '2': listar_produtos()
                        case '3': editar_produto()
                        case '4': excluir_produto()
                        case '0': break
                        case _: print(mensagens["opcao_invalida"])
            case '4':
                while True:
                    print(mensagens["menu_compras"])
                    opcao_compra = input("Escolha uma opção: ")

                    match opcao_compra:
                        case '1': criar_compra()
                        case '2': listar_compras()
                        case '3': cancelar_ultima_compra()
                        case '0': break
                        case _: print(mensagens["opcao_invalida"])
            case '0':
                print("Saindo...")
                break
            case _:
                print(mensagens["opcao_invalida"])

if __name__ == '__main__':
    menu()
