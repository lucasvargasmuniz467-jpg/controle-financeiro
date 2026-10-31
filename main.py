
movimentacoes = []

def cadastrar_movimentacao():
    tipo = input("Receita ou despesa? (R/D): ").upper()

    if tipo not in ["R", "D"]:
        print("Tipo inválido!")
        return

    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    valor = float(input("Valor em reais: "))

    movimentacao = {
        "tipo": tipo,
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    movimentacoes.append(movimentacao)
    print("Movimentação cadastrada!")

def consultar_saldo():
    saldo = 0

    for movimentacao in movimentacoes:
        if movimentacao["tipo"] == "R":
            saldo += movimentacao["valor"]
        else:
            saldo -= movimentacao["valor"]

    print(f"Saldo atual: R$ {saldo:.2f}")

def listar_movimentacoes():
    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return

    for item in movimentacoes:
        tipo = "Receita" if item["tipo"] == "R" else "Despesa"

        print(
            f"{tipo} | {item['descricao']} | "
            f"{item['categoria']} | R$ {item['valor']:.2f}"
        )

while True:
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Cadastrar movimentação")
    print("2 - Consultar saldo")
    print("3 - Listar movimentações")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_movimentacao()
    elif opcao == "2":
        consultar_saldo()
    elif opcao == "3":
        listar_movimentacoes()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
