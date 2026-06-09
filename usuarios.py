from validacao import (
    validar_nome,
    validar_email,
    validar_senha
)

def cadastrar_usuario(lista_usuarios):

    nome = input("Nome: ")

    if not validar_nome(nome):
        print("Nome inválido.")
        return

    email = input("Email: ")

    if not validar_email(email):
        print("Email inválido.")
        return

    senha = input("Senha: ")

    if not validar_senha(senha):
        print("Senha inválida.")
        return

    lista_usuarios.append({
        "nome": nome,
        "email": email,
        "senha": senha
    })

    print("Cadastro realizado.")
def buscar_usuario(email, lista_usuarios):

    for nome, dados in lista_usuarios.items():

        if dados["email"] == email:
            return {"nome": nome, **dados}

    return None
    
def login(lista_usuarios):

    email = input("Email: ")
    senha = input("Senha: ")

    usuario = buscar_usuario(email, lista_usuarios)

    if usuario and usuario["senha"] == senha:
        return usuario

    return None