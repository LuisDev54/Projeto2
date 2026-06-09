def validar_nome(nome):
    while True:

            nome = input("Nome: ").strip()

            tem_numero = False
            invalido = False
            i = 0

            while i < len(nome):
                if nome[i] >= "0" and nome[i] <= "9":
                    tem_numero = True
                elif nome[i] != " " and not ("A" <= nome[i] <= "Z") and not ("a" <= nome[i] <= "z"):
                    invalido = True
                i += 1

            if tem_numero == True or invalido == True:
                print("Inválido! O nome só pode ter letras.")
            else:
                break


def validar_email(email):
    while True:
            email = input("Email: ").strip()
            if "@" not in email:
                print("Email inválido!")
            elif "gmail.com" not in email and "hotmail.com" not in email:
                print("Email inválido!")
            elif email[0] == "@":
                print("Email inválido!")
            elif email[-9:] != "gmail.com" and email[-11:] != "hotmail.com":
                print("Email inválido!")
            else:
                break


def validar_senha(senha):
    return len(senha) >= 8


def validar_identificacao(codigo):
    return len(codigo) == 4


def validar_tipo_animal(tipo, tipos):
    return tipo in tipos


def validar_cor_brinco(cor, cores):
    return cor in cores