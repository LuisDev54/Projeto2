from rich.console import Console
from rich.table import Table
console = Console()
from dados import (historico)
from rebanho import (buscar_animal)

def comprar_produto(produtos, historico):

    nome = input("Produto: ")

    if nome not in produtos:
        print("Produto não encontrado.")
        return

    qtd = int(input("Quantidade: "))

    if qtd > produtos[nome]["quantidade"]:
        print("Estoque insuficiente.")
        return

    produtos[nome]["quantidade"] -= qtd

    historico["movimentacoes"].append({
        "data": "hoje",
        "acao": "venda",
        "item": nome,
        "qtd": qtd
    })

    print("Compra realizada com sucesso!")
def comprar_animal(animais, historico):

    codigo = input("Identificação: ")

    if codigo not in animais:
        print("Animal não encontrado.")
        return

    animal = animais[codigo]

    historico["movimentacoes"].append({
        "data": "hoje",
        "acao": "venda",
        "item": animal["tipo"],
        "qtd": 1
    })

    del animais[codigo]

    print("Animal vendido com sucesso!")

historico = {"movimentacoes": []}


def registrar_movimentacao(historico, acao, item, qtd):

    from datetime import datetime

    historico["movimentacoes"].append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "acao": acao,
        "item": item,
        "qtd": qtd
    })
def produzir_queijo(produtos, historico):

    leite = produtos["leite"]["quantidade"]

    qtd = leite // 10

    if qtd > 0:

        produtos["leite"]["quantidade"] -= qtd * 10
        produtos["queijo"]["quantidade"] += qtd

        registrar_movimentacao(
            historico,
            "produção",
            "Queijo",
            qtd
        )

        print(f"{qtd} queijo(s) produzido(s).")
def ver_historico(historico):

    table = Table(title="Histórico de Movimentação")

    table.add_column("Data")
    table.add_column("Ação")
    table.add_column("Item")
    table.add_column("Qtd")

    for mov in historico["movimentacoes"]:
        table.add_row(
            mov["data"],
            mov["acao"],
            mov["item"],
            str(mov["qtd"])
        )

    console.print(table)