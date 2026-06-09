from rich.console import Console
from rich.table import Table
console = Console()
from compras import registrar_movimentacao
from dados import (historico)
def buscar_produto(nome, produtos):

    return produtos.get(nome)
def cadastrar_produto(produtos, historico):

    nome = input("Nome: ")

    if nome in produtos:
        print("Produto já cadastrado!")
        return

    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    produtos[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }
    registrar_movimentacao(
    historico,
    "cadastro",
    nome,
    quantidade
)

    print("Produto cadastrado com sucesso!")
def listar_produtos(produtos):

    table = Table(title="Produtos")

    table.add_column("Nome")
    table.add_column("Quantidade")
    table.add_column("Preço")

    for nome, dados in produtos.items():
        table.add_row(
            nome,
            str(dados["quantidade"]),
            str(dados["preco"])
        )

    console.print(table)
def remover_produto(produtos, historico):

    nome = input("Produto: ")

    produto = buscar_produto(nome, produtos)

    if produto:
        del produtos[nome]
        print("Produto removido com sucesso!")
        registrar_movimentacao(
    historico,
    "remoção",
    nome,
    produtos[nome]["quantidade"]
)
    else:
        print("Produto não encontrado.")