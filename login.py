import re
import json
import menu

def valida_nome(nome):
    return bool(re.match("^[a-zA-ZáéíóúãõâêîôûàèìòùäëïöüçÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙÄËÏÖÜÇ\s]+$", nome))


def valida_cpf(cpf):
    cpf_digits = re.sub(r'\D', '', cpf)

    if len(cpf_digits) != 11:
        return False

    sum1 = sum(int(cpf_digits[i]) * (10 - i) for i in range(9)) % 11
    verif1 = 0 if sum1 < 2 else 11 - sum1

    sum2 = sum(int(cpf_digits[i]) * (11 - i) for i in range(10)) % 11
    verif2 = 0 if sum2 < 2 else 11 - sum2

    return cpf_digits[-2:] == f'{verif1}{verif2}'


def valida_senha(senha):
    if len(senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres.")
    if not re.search(r'[A-Z]', senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
    if not re.search(r'[a-z]', senha):
        print("A senha deve conter pelo menos uma letra minúscula.")
    if not re.search(r'\d', senha):
        print("A senha deve conter pelo menos um número.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        print("A senha deve conter pelo menos um caractere especial.")
    if len(senha) < 8 or not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'\d',
                                                                                                           senha) or not re.search(
            r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False
    return True


def carregar_usuarios():
    try:
        with open('usuarios.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)


def adicionar_usuario(cpf, nome, senha):
    usuarios = carregar_usuarios()
    usuarios[cpf] = {"nome": nome, "senha": senha}
    salvar_usuarios(usuarios)


while True:
    print("Bem vindo ao site Notredame\n1- Entrar\n2- Criar Usuário")
    decisao = input()

    match decisao:
        case '1':
            usuarios = carregar_usuarios()
            while True:
                cpf = input("Digite seu cpf: ")
                if valida_cpf(cpf):
                    print(f'O CPF {cpf} é válido.')
                    break
                else:
                    print(f'O CPF {cpf} é inválido.')

            while True:
                senha = input("Digite sua senha: ")
                if not valida_senha(senha):
                    print("Erro: Senha inválida!")
                elif usuarios.get(cpf, {}).get("senha") != senha:
                    print("Erro: Senha não cadastrada no banco de dados!")
                else:
                    print("Entrou com sucesso :)")
                    menu.informacoes(cpf, usuarios[cpf]["nome"], senha)


        case '2':
            while True:
                cpf = input("Digite seu cpf: ")
                cpf = re.sub(r'\D', '', cpf)
                if valida_cpf(cpf) and not carregar_usuarios().get(cpf):
                    break
                else:
                    print("Erro: CPF inválido ou já cadastrado.")

            while True:
                senha = input("Digite sua senha: ")
                if valida_senha(senha):
                    break
                else:
                    print("Erro: Senha inválida.")

            while True:
                nome = input("Digite seu nome: ")
                if valida_nome(nome):
                    break
                else:
                    print("Erro: O nome deve conter apenas letras, espaços e acentos.")

            adicionar_usuario(cpf, nome, senha)
            print("Usuário adicionado com sucesso!")

        case _:
            print("Digite um número válido!")
