import json
import re
from datetime import datetime


def valida_conv(numero):
    numeros = re.findall(r'\d', str(numero))
    numeros.extend(['0'] * (10 - len(numeros)))
    numero_formatado = re.sub(r'(\d{3})(\d{3})(\d{6})(\d{1,4})?', r'\1 \2 \3 \4', ''.join(numeros))
    return numero_formatado


def valida_data_nascimento(data_nascimento):
    try:
        data_formatada = datetime.strptime(data_nascimento, '%d/%m/%Y')

        if not 1900 <= data_formatada.year <= datetime.now().year:
            return False

        return True
    except ValueError:
        return False


def valida_rg_formato(rg):
    rg_formato = re.match(r'^\d{9}$', rg)
    return rg_formato is not None


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
            if valida_rg_formato(rg):
                break
            else:
                print("RG inválido! formatação (xxxxxxxxx)\nNão precisa de ./-")
        while True:
            nascimento = input("Digite sua data de nascimento: ")
            if valida_data_nascimento(nascimento):
                break
            else:
                print("Data de nascimento inválida!")
        while True:
            carteira_conve = input("Digite o número da carteira do convênio: ")
            if valida_conv(carteira_conve):
                break
            else:
                print("Número errado! formatação (xxx xxx xxxxxx xxx)")
