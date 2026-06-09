from config import LEITE_POR_QUEIJO, PRECO_QUEIJO, PRECO_LEITE
from dados import (usuarioADM, usuarioCLI, animais, produtos, historico, registrar_movimentacao)
from usuarios import (login,cadastrar_usuario)
from rebanho import (cadastrar_animal, listar_animais, remover_animal, atualizar_status)
from produtos import (cadastrar_produto,listar_produtos,remover_produto)
from compras import (comprar_animal,comprar_produto, ver_historico,)
from transportadora import (agendar_transporte,listar_agendamentos)
from rich.console import Console
from rich.table import Table
console = Console()

def menu_login():

    op = input("1 - Administrador\n2 - Cliente\nOpção: ")

    email = input("Email: ")
    senha = input("Senha: ")

    encontrado = False

 
    if op == "1":

        for nome, usuario in usuarioADM.items():

            if usuario["email"] == email and usuario["senha"] == senha:

                print(f"Bem-vindo ADM {nome}!")
                encontrado = True
                menu_administrador()
                break

        if not encontrado:
            print("Login inválido.")

    elif op == "2":

        for nome, usuario in usuarioCLI.items():

            if usuario["email"] == email and usuario["senha"] == senha:

                print(f"Bem-vindo Cliente {nome}!")
                encontrado = True
                menu_cliente()
                break

        if not encontrado:
            print("Login inválido.")


def menu_cadastro():

    print("1 - Administrador")
    print("2 - Cliente")

    op = input("Opção: ")

    if op == "1":
        cadastrar_usuario(usuarioADM)

    elif op == "2":
        cadastrar_usuario(usuarioCLI)

def menu_principal():

    while True:
        console.print("\n[bold cyan]=== AGRO APP ===[/bold cyan]")
        console.print("[1] Login")
        console.print("[2] Cadastro")
        console.print("[0] Sair")

        op = input("Opção: ")

        if op == "1":
            menu_login()
        elif op == "2":
            menu_cadastro()
        elif op == "0":
            break

def menu_administrador():

    while True:

        print("1 - Gerenciar Rebanho")
        print("2 - Gerenciar Produção e Derivados")
        print("3 - Dashboard")
        print("4 - Produção de Queijo")
        print("5 - histórico de movimentação")
        print("0 - Voltar")

        op = int(input("Opção: "))

        if op == 1:
            menu_rebanho()

        elif op == 2:
            menu_produtos()
        
        elif op == 3:
            dashboard_fazenda(animais, produtos)

        elif op == 4:
            produzir_queijo(produtos, historico)

        elif op == 5:
            ver_historico(historico)

        elif op == 0:
            break

def menu_cliente():

    while True:

        print("1 - Comprar Animal")
        print("2 - Comprar Produto")
        print("3 - Transporte")
        print("0 - Voltar")

        op = int(input("Opção: "))

        if op == 1:
            comprar_animal(animais)

        elif op == 2:
            comprar_produto(produtos,historico)

        elif op == 3:
            agendar_transporte()

        elif op == 0:
            break
def menu_rebanho():
                while True:

                    print("\n=== REBANHO ===")
                    print("1 - Listar animais")
                    print("2 - Cadastrar animal")
                    print("3 - Remover animal")
                    print("0 - Voltar")

                    op = input("Opção: ")

                    if op == "1":
                        listar_animais(animais)

                    elif op == "2":
                        cadastrar_animal(animais)

                    elif op == "3":
                        remover_animal(animais)

                    elif op == "0":
                        break
def menu_produtos():

    while True:

        print("\n=== PRODUTOS ===")
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Remover produto")
        print("0 - Voltar")

        op = input("Opção: ")

        if op == "1":
            listar_produtos(produtos)

        elif op == "2":
            cadastrar_produto(produtos)

        elif op == "3":
            remover_produto(produtos)
        elif op == "0":
            break

        else:
            print("Opção inválida!")

def dashboard_fazenda(animais, produtos):

    console.print("\n[bold green]DASHBOARD DA FAZENDA[/bold green]\n")

    table = Table(title="Estoque de Produtos")

    table.add_column("Produto", style="cyan")
    table.add_column("Quantidade", style="magenta")

    for nome, dados in produtos.items():
        table.add_row(nome, str(dados["quantidade"]))

    console.print(table)
    console.print("\n[bold]CONFIGURAÇÕES DO SISTEMA[/bold]")
    console.print(f"Leite por queijo: {LEITE_POR_QUEIJO}")
    console.print(f"Preço leite: {PRECO_LEITE}")
    console.print(f"Preço queijo: {PRECO_QUEIJO}")
def produzir_queijo(produtos, historico):

    leite = produtos.get("leite", {}).get("quantidade", 0)

    if leite < LEITE_POR_QUEIJO:
        print("Leite insuficiente.")
        return

    quantidade = leite // LEITE_POR_QUEIJO

    produtos["leite"]["quantidade"] -= quantidade * LEITE_POR_QUEIJO

    if "queijo" not in produtos:
        produtos["queijo"] = {"quantidade": 0, "preco": 0}

    produtos["queijo"]["quantidade"] += quantidade

    historico["movimentacoes"].append({
        "data": "produção",
        "acao": "produção",
        "item": "Queijo",
        "qtd": quantidade
    })

    print(f"{quantidade} queijo(s) produzidos!")