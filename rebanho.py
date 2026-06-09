from rich.console import Console
from rich.table import Table
console = Console()
from dados import (historico, registrar_movimentacao)
from dados import (
    TIPOS_ANIMAIS,
    CORES_BRINCO,
    STATUS_ANIMAIS
)

from validacao import (
    validar_identificacao
)
def buscar_animal(codigo, animais):

    return animais.get(codigo)

def cadastrar_animal(animais):

    print(TIPOS_ANIMAIS)
    print("-" * 10)
    while True:
        tipo = input("Escolha o tipo: ").lower()

        if tipo not in TIPOS_ANIMAIS:
            print("Tipo inválido!")
            return
        break

    print("Cores disponíveis: azul, amarelo, verde")
    print("-" * 10)

    brinco = input("Escolha a cor do brinco: ").lower()

    if brinco not in CORES_BRINCO:
        print("Cor inválida!")
        return

    print("Dica: a identificação pode usar letras e números (ex: A004)")
    codigo = input("Identificação: ")

    if not validar_identificacao(codigo):
        print("Identificação inválida!")
        return

    
    if codigo in animais:
        print("Animal já cadastrado!")
        return

    animais[codigo] = {
        "tipo": tipo,
        "brinco": brinco,
        "identificacao": codigo,
        "status": STATUS_ANIMAIS[3]
    }
    registrar_movimentacao(
    historico,
    "cadastro",
    "Animal " + codigo,
    1
)
    print("Animal cadastrado com sucesso!")
def listar_animais(animais):

    table = Table(title="Rebanho")

    table.add_column("Tipo")
    table.add_column("Identificação")
    table.add_column("Status")

    for animal in animais:
        table.add_row(
            animal["tipo"],
            animal["identificacao"],
            animal["status"]
        )

    console.print(table)
def remover_animal(animais):

    codigo = input("Identificação: ")

    animal = buscar_animal(codigo, animais)

    if animal:
        del animais[codigo]
        print("Animal removido com sucesso!")
        registrar_movimentacao(
        historico,
        "remoção",
        animal["tipo"],
        1
    )
    else:
        print("Animal não encontrado.")
def atualizar_status(animais, historico):

    codigo = input("Identificação do animal: ")

    if codigo not in animais:
        print("Animal não encontrado.")
        return

    print("Status disponíveis: ativo, vendido, doente, morto")
    novo_status = input("Novo status: ").lower()

    animais[codigo]["status"] = novo_status

    registrar_movimentacao(
        historico,
        "status",
        animais[codigo]["tipo"] + " -> " + novo_status,
        1
    )

    print("Status atualizado com sucesso!")