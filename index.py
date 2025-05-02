# Loja de Comidas
from loja import lojas, criar_loja, listar_lojas, editar_loja, excluir_loja
from cliente import clientes, criar_cliente, listar_clientes, editar_cliente, excluir_cliente
from produto import produtos, criar_produto, listar_produtos, editar_produto, excluir_produto
from compra import compras, criar_compra, listar_compras, editar_compra, excluir_compra

mensagens = {
    "menu_principal": "Menu Principal \n 1. Opções Clientes \n 2. Opções Lojas \n 3. Opções Produtos \n 4. Opções Compras \n 0. Sair",
    "menu_clientes": "Menu Clientes \n 1. Criar Cliente \n 2. Listar Clientes \n 3. Editar Cliente \n 4. Excluir Cliente \n 0. Voltar",
    "menu_lojas": "Menu Lojas \n 1. Criar Loja \n 2. Listar Lojas \n 3. Editar Loja \n 4. Excluir Loja \n 0. Voltar",
    "menu_produtos": "Menu Produtos \n 1. Criar Produto \n 2. Listar Produtos \n 3. Editar Produto \n 4. Excluir Produto \n 0. Voltar",
    "menu_compras": "Menu Compras \n 1. Criar Compra \n 2. Listar Compras \n 3. Editar Compra \n 4. Excluir Compra \n 0. Voltar",
    "opcao_invalida": "Opção inválida. Tente novamente.",
}

def main():
    while True:
        print(mensagens["menu_principal"])
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                while True:
                    print(mensagens["menu_clientes"])
                    opcao_cliente = input("Escolha uma opção: ")

                    match opcao_cliente:
                        case '1':
                            criar_cliente()
                        case '2':
                            listar_clientes()
                        case '3':
                            editar_cliente()
                        case '4':
                            excluir_cliente()
                        case '0':
                            break
                        case _:
                            print(mensagens["opcao_invalida"])
                            continue
            case '2':
                while True:
                    print(mensagens["menu_lojas"])
                    opcao_loja = input("Escolha uma opção: ")

                    match opcao_loja:
                        case '1':
                            criar_loja()
                        case '2':
                            listar_lojas()
                        case '3':
                            editar_loja()
                        case '4':
                            excluir_loja()
                        case '0':
                            break
                        case _:
                            print(mensagens["opcao_invalida"])
                            continue
            case '3':
                while True:
                    print(mensagens["menu_produtos"])
                    opcao_produto = input("Escolha uma opção: ")

                    match opcao_produto:
                        case '1':
                            criar_produto()
                        case '2':
                            listar_produtos()
                        case '3':
                            editar_produto()
                        case '4':
                            excluir_produto()
                        case '0':
                            break
                        case _:
                            print(mensagens["opcao_invalida"])
                            continue
            case '4':
                while True:
                    print(mensagens["menu_compras"])
                    opcao_compra = input("Escolha uma opção: ")

                    match opcao_compra:
                        case '1':
                            criar_compra()
                        case '2':
                            listar_compras()
                        case '3':
                            editar_compra()
                        case '4':
                            excluir_compra()
                        case '0':
                            break
                        case _:
                            print(mensagens["opcao_invalida"])
                            continue
            case '0':
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue
        print("\n" + "-" * 30 + "\n")

    ...

if __name__ == '__main__':
    main()