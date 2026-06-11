import time
from pathlib import Path

def carregar_dados():
    dados = {}

    arquivo = Path("estacionamento.txt")

    if not arquivo.is_file():
        return dados
    
    with open("estacionamento.txt", "r", encoding="utf-8") as arquivo:

        for linha in arquivo:
            placa, marca, modelo, horaEntrada = linha.strip().split(";")

            dados[placa] = {
                "marca" : marca,
                "modelo" : modelo,
                "horaEntrada": horaEntrada
            }

    return dados

def salvar_dados(dados):
    with open("estacionamento.txt", "w", encoding="utf-8") as arquivo:

        for placa, veiculo in dados.items():
             arquivo.write(
                f"{placa};"
                f"{veiculo['marca']};"
                f"{veiculo['modelo']};"
                f"{veiculo['horaEntrada']}\n"
            )

def menu():

    while True:


        print("Estacionamento Rotativo")
        print("1. Entrada veículo")
        print("2. Saída veículo")
        print("3. Listar veículo")
        print("4. Buscar veículo")
        print("5. Total recebido no dia")
        print("6. Sair")

        op = int(input("Opção: "))

        if 1 <= op <= 6:
            return op
            
        print("Opção inválida. Você deve escolher uma opção entre 1 e 6.")

def adicionar_veiculos(dados):
    placa = input("Digite o código da placa: ")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    horaEntrada = input("Digite a hora de entrada (HH:MM): ")

    if placa == "":
        print("A placa é obrigatório. Tente novamente.")
        return
    
    if placa in dados:
        print("Já existe um veículo com essa placa.")
        return
        
    dados[placa] = {
        "marca": marca,
        "modelo" : modelo,
        "horaEntrada": horaEntrada
    }
    print("Veículo cadastrado com sucesso!")

def listar_veiculos(dados):
    if len(dados) == 0:
        print("Nenhum veículo cadastrado.")
        return
    
    for index, placa in enumerate(sorted(dados.keys()),start=1):
        veiculo = dados[placa]
        print(
            f"{index}."
            f"Placa:{placa}|"
            f"Marca:{veiculo['marca']}|"
            f"Entrada:{veiculo['horaEntrada']}"
        )

dados = carregar_dados()

op = menu()

while op != 6:
    if op == 1:
        adicionar_veiculos(dados)
    
    if op == 3:
        listar_veiculos(dados)

    
    time.sleep(2)
    op = menu()

salvar_dados(dados)