cupons = [
    {
        "codigo": "DESCONTO10",
        "desconto": 10,
    }
]


def adicionar_cupom():
    codigo = input("Digite o código do cupom: ").strip().upper()
    desconto = int(input("Digite o valor do desconto: "))
    if not desconto:
        print("O valor do desconto não pode ser vazio.")
        return
    if not codigo:
        print("O código do cupom não pode ser vazio.")
        return
    cupom = {
        "codigo": codigo,
        "desconto": desconto,
    }
    cupons.append(cupom)
    print("Cupom adicionado com sucesso!")


def listar_cupons():
    if not cupons:
        print("Nenhum cupom cadastrado.")
        return
    print("\n--- Lista de Cupons ---")
    for cupom in cupons:
        print(f"Código: {cupom['codigo']}, Desconto: R${cupom['desconto']:.2f}")


def editar_cupom():
    if not cupons:
        print("Nenhum cupom cadastrado.")
        return
    listar_cupons()
    codigo = input("Digite o código do cupom que deseja editar: ").strip().upper()
    for cupom in cupons:
        if cupom["codigo"] == codigo:
            novo_codigo = (
                input("Novo código (pressione Enter para manter): ").strip().upper()
            )
            novo_desconto = input(
                "Novo valor de desconto (pressione Enter para manter): "
            ).strip()
            if novo_codigo:
                cupom["codigo"] = novo_codigo
            if novo_desconto:
                try:
                    desconto = float(novo_desconto)
                    if desconto < 0:
                        print("O desconto deve ser um valor positivo.")
                        return
                    cupom["desconto"] = desconto
                except ValueError:
                    print("Valor de desconto inválido.")
                    return
            print("Cupom atualizado com sucesso!")
            return
    print("Cupom não encontrado.")


def excluir_cupom():
    if not cupons:
        print("Nenhum cupom cadastrado.")
        return
    listar_cupons()
    codigo = input("Digite o código do cupom a ser removido: ").strip().upper()
    for cupom in cupons:
        if cupom["codigo"] == codigo:
            cupons.remove(cupom)
            print("Cupom removido com sucesso!")
            return
    print("Cupom não encontrado.")


def pegar_cupom_por_codigo(codigo):
    for cupom in cupons:
        if cupom["codigo"] == codigo:
            return cupom
    return None
