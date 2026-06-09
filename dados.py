usuarioADM = {
    "wallisson": {
        "email": "wallisson123@gmail.com",
        "senha": "#agronegócio"
    },
    "guilherme": {
        "email": "guigui@gmail.com",
        "senha": "@algoritmos"
    },
    "renê": {
        "email": "gadelha@gmail.com",
        "senha": "coordenadoria26"
    },
    "gilvan": {
        "email": "reigil@gmail.com",
        "senha": "gilvanII"
    }
}
usuarioCLI = {
    "gabriel": {
        "email": "gabrielbastos@gmail.com",
        "senha": "zecabode"
    },
    "zacarias": {
        "email": "zacarias01@gmail.com",
        "senha": "fazendajatobar###"
    }
}
animais = {
    "A001": {
        "tipo": "bovino",
        "brinco": "azul",
        "status": "em lactação"
    },
    "A002": {
        "tipo": "bovino",
        "brinco": "verde",
        "status": "engorda"
    },
    "A003": {
        "tipo": "caprino",
        "brinco": "amarelo",
        "status": "venda"
    }
}
produtos = {
    "leite": {
        "quantidade": 100,
        "preco": 5.00
    },
    "queijo": {
        "quantidade": 50,
        "preco": 9.00
    }
}

STATUS_ANIMAIS = {
    1: "em lactacao",
    2: "engorda",
    3: "venda"
}

TIPOS_ANIMAIS = { "bovino","ovino","caprino","suino","ave"}

CORES_BRINCO = {
    "azul": True,
    "verde": True,
    "amarelo": True,
    "vermelho": True
}
historico = {"movimentacoes": []}

def registrar_movimentacao(historico, acao, item, qtd):
    from datetime import datetime

    historico["movimentacoes"].append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "acao": acao,
        "item": item,
        "qtd": qtd
    })