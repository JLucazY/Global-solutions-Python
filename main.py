import json
import re
from datetime import datetime


def valida_data_nascimento(data_nascimento):
    try:
        data_formatada = datetime.strptime(data_nascimento, '%d/%m/%Y')

        if not 1900 <= data_formatada.year <= datetime.now().year:
            return False

        return True
    except ValueError:
        return False

def valida_rg(rg):
    rg_numerico = re.sub(r'\D', '', rg)

    if len(rg_numerico) != 9:
        return False

    if not 1 <= int(rg_numerico[0]) <= 9:
        return False

    soma = 0
    for i in range(2, 10):
        soma += int(rg_numerico[i - 1]) * (11 - i)

    resto = soma % 11
    dv_calculado = 11 - resto if resto > 1 else 0

    if dv_calculado != int(rg_numerico[8]):
        return False

    return True


def informacoes(cpf, nome, senha):
    print(f"\nSeja Bem Vindo {nome}!\nAgora você tem acesso a todas nossas funcionalidades.")


def carregar_usuarios():
    try:
        with open('dados_convenio.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_usuarios(dados):
    with open('dados_convenio.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def adicionar_usuario(cpf, nome, senha):
    dados = carregar_usuarios()
    dados[rg] = {"nome": nome, "senha": senha}
    salvar_usuarios(dados)


decisao = input("""
1 - Adicionar dados do convênio
2 - Agendar consulta
3 - Exibir dados do convênio
4 - Sair
""")

match decisao:
    case '1':
        print("Adicione os dados!")
        while True:
            rg = input("Digite seu rg: ")
            if valida_rg(rg):
                break
            else:
                print("RG inválido!")
        while True:
            nascimento = input("Digite sua data de nascimento: ")
            if valida_data_nascimento(nascimento):
                break
            else:
                print("Data de nascimento inválida!")
        carteira_conve = input("Digite o número da carteira do convênio: ")
