import json
import os
from time import sleep


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


# Caminho do arquivo JSON
arquivo_reservas = 'reservas.json'
arquivo_pontos_turisticos = 'pontos_turisticos.json'


# Funções CRUD para Reservas
def adicionar_reserva(nome, cpf):
    try:
        with open(arquivo_reservas, 'r') as f:
            reservas = json.load(f)
    except FileNotFoundError:
        reservas = []

    for reserva in reservas:
        if reserva['cpf'] == cpf:
            print("😡 CPF JÁ CADASTRADO COM OUTRO NOME!")
            return

    reservas.append({'nome': nome, 'cpf': cpf, 'destino': None})

    with open(arquivo_reservas, 'w') as f:
        json.dump(reservas, f, indent=4)
    print("😎 RESERVA ADICIONADA COM SUCESSO!")
    print("=" * 50)


def listar_reservas():
    try:
        with open(arquivo_reservas, 'r') as f:
            reservas = json.load(f)
    except FileNotFoundError:
        reservas = []

    if reservas:
        print("=" * 50)
        print("LISTA DE RESERVAS:")
        print("=" * 50)
        for reserva in reservas:
            print(f"NOME: {reserva['nome']}, CPF: {reserva['cpf']}, DESTINO: {reserva['destino']}")
            print("=" * 50)
    else:
        print("😒 NENHUMA RESERVA CADASTRADA.")


def atualizar_reserva(nome, novo_cpf):
    try:
        with open(arquivo_reservas, 'r') as f:
            reservas = json.load(f)
    except FileNotFoundError:
        reservas = []

    for reserva in reservas:
        if reserva['nome'] == nome:
            reserva['cpf'] = novo_cpf
            with open(arquivo_reservas, 'w') as f:
                json.dump(reservas, f, indent=4)
            print("😙 RESERVA ATUALIZADA COM SUCESSO!")
            print("=" * 50)
            return

    print("😒 RESERVA NÃO ENCONTRADA.")
    print("=" * 50)


def cancelar_reserva(nome):
    try:
        with open(arquivo_reservas, 'r') as f:
            reservas = json.load(f)
    except FileNotFoundError:
        reservas = []

    for reserva in reservas:
        if reserva['nome'] == nome:
            reservas.remove(reserva)
            with open(arquivo_reservas, 'w') as f:
                json.dump(reservas, f, indent=4)
            print("😡 RESERVA CANCELADA COM SUCESSO!")
            print("=" * 50)
            return

    print("😒 RESERVA NÃO ENCONTRADA.")
    print("=" * 50)


def confirmar_destino(nome, destino):
    destinos_validos = {
        "1": "Porto de Galinhas",
        "2": "Paris",
        "3": "Rio de Janeiro",
        "4": "Orlando",
        "5": "China",
        "6": "Cancun"
    }

    try:
        with open(arquivo_reservas, 'r') as f:
            reservas = json.load(f)
    except FileNotFoundError:
        reservas = []

    for reserva in reservas:
        if reserva['nome'] == nome:
            reserva['destino'] = destinos_validos.get(destino, None)
            if reserva['destino'] is None:
                print("😡 DESTINO INVÁLIDO!")
                return
            with open(arquivo_reservas, 'w') as f:
                json.dump(reservas, f, indent=4)
            print("😎 DESTINO CONFIRMADO COM SUCESSO!")
            print("=" * 50)
            return

    print("😒 RESERVA NÃO ENCONTRADA.")
    print("=" * 50)


def buscar_reserva(nome):
    try:
        with open(arquivo_reservas, 'r') as f:
            reservas = json.load(f)
    except FileNotFoundError:
        reservas = []

    encontrado = False

    for reserva in reservas:
        if reserva['nome'] == nome:
            print(f"NOME: {reserva['nome']}, CPF: {reserva['cpf']}, DESTINO: {reserva['destino']}")
            encontrado = True
    if not encontrado:
        print("😒 NENHUMA RESERVA CADASTRADA.")


def menu_inicial():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.CIANO + " ------> BEM VINDO AO SISTEMA REDDG DE RESERVAS <------ ")
    print("         OPÇÃO 1 - SOBRE RESERVAS ")
    print("         OPÇÃO 2 - SOBRE DESTINOS ")
    print("         OPÇÃO 3 - PARA SAIR ")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def exibir_menu_reservas():
    print("\nMENU RESERVAS:")
    print("1. ADICIONAR RESERVA")
    print("2. LISTAR RESERVAS")
    print("3. ATUALIZAR RESERVA")
    print("4. CANCELAR RESERVA")
    print("5. BUSCAR RESERVA")
    print("6. VOLTAR AO MENU ANTERIOR")


def exibir_menu_destinos():
    print("\nMENU DESTINOS:")
    print("1. CONFIRMAR DESTINO")
    print("2. VOLTAR AO MENU ANTERIOR")
    print("")


def exibir_detalhes_destino(destino_id):
    try:
        with open(arquivo_pontos_turisticos, 'r') as f:
            pontos_turisticos = json.load(f)
    except FileNotFoundError:
        pontos_turisticos = []

    for ponto in pontos_turisticos:
        if ponto['id'] == destino_id:
            print(f"Nome: {ponto['nome']}")
            print(f"Descrição: {ponto['descricao']}")
            print(f"Horários: {ponto['horarios']}")
            print(f"Custo: {ponto['custo']}")
            print("Avaliações:")
            for avaliacao in ponto['avaliacoes']:
                print(f" - {avaliacao['usuario']}: {avaliacao['comentario']}")
            print("=" * 50)
            return

    print("😒 DETALHES DO DESTINO NÃO ENCONTRADOS.")


def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        if opcao_inicial == 1:
            while True:
                exibir_menu_reservas()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                if opcao == "1":
                    nome = input(" DIGITE O NOME:\n>>> ")
                    cpf = input(" DIGITE O CPF:\n>>> ")
                    adicionar_reserva(nome, cpf)
                elif opcao == "2":
                    listar_reservas()
                elif opcao == "3":
                    nome = input("DIGITE O NOME A SER ATUALIZADO:\n>>> ")
                    novo_cpf = input("DIGITE O NOVO CPF:\n>>> ")
                    atualizar_reserva(nome, novo_cpf)
                elif opcao == "4":
                    nome = input("DIGITE O NOME DA RESERVA A SER CANCELADA:\n>>> ")
                    cancelar_reserva(nome)
                elif opcao == "5":
                    nome = input("DIGITE O NOME DA RESERVA:\n>>> ")
                    buscar_reserva(nome)
                elif opcao == "6":
                    print("VOLTANDO AO MENU ANTERIOR...")
                    sleep(3)
                    break
                else:
                    print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
        elif opcao_inicial == 2:
            while True:
                exibir_menu_destinos()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                if opcao == "1":
                    print("ESCOLHA UM DESTINO:")
                    print("1. Porto de Galinhas")
                    print("2. Paris")
                    print("3. Rio de Janeiro")
                    print("4. Orlando")
                    print("5. China")
                    print("6. Cancun")
                    destino_id = input(">>> ")
                    confirmar_destino(nome, destino_id)
                    exibir_detalhes_destino(int(destino_id))
                elif opcao == "2":
                    print("VOLTANDO AO MENU ANTERIOR...")
                    sleep(3)
                    break
                else:
                    print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
        elif opcao_inicial == 3:
            print("🚀 SAINDO...")
            sleep(3)
            break
        else:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main()

