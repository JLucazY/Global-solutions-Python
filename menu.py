import re
from datetime import datetime
import random

dados_convenio = {}


def horario_medico():
    num = random.randint(1, 5)
    if num == 1:
        return "11:30"
    elif num == 2:
        return "14:00"
    elif num == 3:
        return "11:00"
    elif num == 4:
        return "10:30"
    else:
        return "9:00"


def valida_formato_numero(numero):
    numero_sem_espacos = re.sub(r'\s', '', numero)
    if re.match(r'^\d{3}\d{3}\d{6}\d{1,4}$', numero_sem_espacos):
        return True
    else:
        return False


def valida_data_nascimento(data_nascimento):
    try:
        data_formatada = datetime.strptime(data_nascimento, '%d/%m/%Y')

        if not 1900 <= data_formatada.year <= datetime.now().year:
            return False

        return True
    except ValueError:
        return False


def main(cpf, nome):
    while True:
        print(f"\nSeja Bem Vindo {nome}!\nAgora você tem acesso a todas nossas funcionalidades.")
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
                    nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
                    if valida_data_nascimento(nascimento):
                        break
                    else:
                        print("Data de nascimento inválida!")


                while True:
                    carteira_conve = input("Digite o número da carteira do convênio: ")
                    if valida_formato_numero(carteira_conve) :
                        break
                    else:
                        print("Número inválido! Formatação correta: xxx xxx xxxxxx xxx")

                dados_convenio[cpf] = {
                    "data_nascimento": nascimento,
                    "carteira_convenio": carteira_conve
                }

                print("Dados adicionados com sucesso")


            case '2':
                while True:
                    print("Selecione o que deseja agendar:\n1 - Psiquiatra\n2 - Neurologista\n3 - Dermatologista\n4 - Cardiologista\n5 - Sair")
                    medico = input()

                    match medico:

                        case '1':
                            while True:
                                print("Qual dia você quer que sua consulta seja?")
                                dia_consulta = input()
                                horario = horario_medico()

                                if dia_consulta.isdigit() and 1 <= int(dia_consulta) <= 31:
                                    dados_convenio[cpf]["consulta_psi"] = f"consulta com o psquiatra para o dia {dia_consulta}/12 ás {horario}"

                                    print(f"Sua consulta com Psiquiatra foi marcada para o dia {dia_consulta}/12 às {horario}")
                                    break

                                else:
                                    print("Dia de consulta inválido! Digite um número de 1 a 31.")


                        case '2':
                            while True:
                                print("Qual dia você quer que sua consulta seja?")
                                dia_consulta = input()
                                horario = horario_medico()

                                if dia_consulta.isdigit() and 1 <= int(dia_consulta) <= 31:
                                    dados_convenio[cpf]["consulta_neu"] = f"consulta com o neurologista para o dia {dia_consulta}/12 ás {horario}"

                                    print(f"Sua consulta com Neurologista foi marcada para o dia {dia_consulta}/12 às {horario}")
                                    break

                                else:
                                    print("Dia de consulta inválido! Digite um número de 1 a 31.")

                        case '3':
                            while True:
                                print("Qual dia você quer que sua consulta seja?")
                                dia_consulta = input()
                                horario = horario_medico()

                                if dia_consulta.isdigit() and 1 <= int(dia_consulta) <= 31:
                                    dados_convenio[cpf]["consulta_der"] = f"consulta com o dermatologista para o dia {dia_consulta}/12 ás {horario}"

                                    print(f"Sua consulta com Dermatologista foi marcada para o dia {dia_consulta}/12 às {horario}")
                                    break

                                else:
                                    print("Dia de consulta inválido! Digite um número de 1 a 31.")

                        case '4':
                            while True:
                                print("Qual dia você quer que sua consulta seja?")
                                dia_consulta = input()
                                horario = horario_medico()

                                if dia_consulta.isdigit() and 1 <= int(dia_consulta) <= 31:
                                    dados_convenio[cpf]["consulta_car"] = f"consulta com o cardiologista para o dia {dia_consulta}/12 ás {horario}"

                                    print(f"Sua consulta com Cardiologista foi marcada para o dia {dia_consulta}/12 às {horario}")
                                    break

                                else:
                                    print("Dia de consulta inválido! Digite um número de 1 a 31.")

                        case '5':
                            break

                        case _:
                            print("Digite os dados corretamente!")

            case '3':
                if cpf in dados_convenio:
                    print("\nDados do Convênio:")
                    print(f"CPF: {cpf}")
                    print(f"Nome: {nome}")
                    print(f"Data de Nascimento: {dados_convenio[cpf]['data_nascimento']}")
                    print(f"Carteira do Convênio: {dados_convenio[cpf]['carteira_convenio']}")

                    consultas = dados_convenio[cpf]
                    if 'consulta_car' in consultas:
                        print(f"Consulta com Cardiologista: {consultas['consulta_car']}")
                    else:
                        print("Não existe registro de consulta marcada com cardiologista")

                    if 'consulta_der' in consultas:
                        print(f"Consulta com Dermatologista: {consultas['consulta_der']}")
                    else:
                        print("Não existe registro de consulta marcada com dermatologista")

                    if 'consulta_neu' in consultas:
                        print(f"Consulta com Neurologista: {consultas['consulta_neu']}")
                    else:
                        print("Não existe registro de consulta marcada com neurologista")

                    if 'consulta_psi' in consultas:
                        print(f"Consulta com Psiquiatra: {consultas['consulta_psi']}")
                    else:
                        print("Não existe registro de consulta marcada com psiquiatra")

                else:
                    print("Preencha com os dados primeiro!")

            case '4':
                quit()

            case _:
                print("Preencha os dados corretamente!")

