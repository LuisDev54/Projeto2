from config import TAXA_TRANSPORTE
meses_31 = {1: "Janeiro", 3: "Março", 5: "Maio", 7: "Julho", 8: "Agosto", 10: "Outubro", 12: "Dezembro"}

meses_30 = {4: "Abril", 6: "Junho", 9: "Setembro", 11: "Novembro"}

agendamentos = {}

compras_cliente = {}

def agendar_transporte():

    nome = input("Digite seu nome: ")

    while True:

        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))

        data_valida = True

        
        if mes in meses_31:

            if dia < 1 or dia > 31:
                data_valida = False

        
        elif mes in meses_30:

            if dia < 1 or dia > 30:
                data_valida = False

        
        elif mes == 2:

            bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

            if bissexto:

                if dia < 1 or dia > 29:
                    data_valida = False

            else:

                if dia < 1 or dia > 28:
                    data_valida = False

        else:
            data_valida = False

        if data_valida:
            break

        print("Data inválida! Tente novamente.")

   
    while True:

        horario = input("Digite o horário (HH:MM): ")

        if len(horario) == 5 and horario[2] == ":":

            hora = int(horario[:2])
            minuto = int(horario[3:])

            if 0 <= hora <= 23 and 0 <= minuto <= 59:
                break

        print("Horário inválido! Tente novamente.")

    
    codigo = f"AG{len(agendamentos) + 1:03d}"

    agendamentos[codigo] = {
        "cliente": nome,
        "dia": dia,
        "mes": mes,
        "ano": ano,
        "horario": horario
    }

    print(f"Agendamento de transporte criado com sucesso!")
    gerar_ticket(nome, codigo, agendamentos, compras_cliente)
    valor_base = 50
    valor_total = valor_base + TAXA_TRANSPORTE

def listar_agendamentos():

    for agendamento in agendamentos:

        print(agendamentos)

def gerar_ticket(nome, codigo, agendamentos, compras_cliente):
    agendamento = agendamentos[codigo]
    print("\n" + "=" * 60)
    print("TICKET / RECIBO DE CARGA")
    print("=" * 60)

    print(f"Cliente: {nome}")

    print(f"Data: {agendamento['dia']}/{agendamento['mes']}/{agendamento['ano']}")
    print(f"Horário: {agendamento['horario']}")

    print("\nITENS COMPRADOS:")

    dados = compras_cliente.get(nome, {})


    produtos = dados.get("produtos", {})

    if produtos:
        print("\nProdutos:")
        for nome_prod, qtd in produtos.items():
            print(f" - {nome_prod}: {qtd}")
    else:
        print("\nProdutos: nenhum")

    animais = dados.get("animais", {})

    if animais:
        print("\nAnimais:")
        for codigo, animal in animais.items():
            print(f" - {codigo} ({animal['tipo']})")
    else:
        print("\nAnimais: nenhum")

    print("\nStatus: AGUARDANDO RETIRADA")
    print("=" * 60)
