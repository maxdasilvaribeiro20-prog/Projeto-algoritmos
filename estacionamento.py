import time
from pathlib import Path

total_recebido = 0

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

        print("=" * 50)
        print("ESTACIONAMENTO ROTATIVO".center(50))
        print("=" * 50)
        
        print("1. Entrada veículo")
        print("2. Saída veículo")
        print("3. Listar veículo")
        print("4. Buscar veículo")
        print("5. Total recebido no dia")
        print("6. Sair")

        op = input("Opção: ")
        
        if not op.isdigit():
            print("Por favor digite só os números da tabela.")
            continue

        op = int(op)

        if 1 <= op <= 6:
            return op
            
        print("Opção inválida. Você deve escolher uma opção entre 1 e 6.")

def adicionar_veiculos(dados):
    placa = input("Digite o código da placa: ").upper()
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    horaEntrada = input("Digite a hora de entrada (HH:MM): ")

    if placa == "" or horaEntrada == "":
        print("A placa e a hora de entrada são obrigatórios. Tente novamente.")
        return
    
    if placa in dados:
        print("Já existe um veículo com essa placa.")
        return
        
    dados[placa] = {
        "marca": marca,
        "modelo" : modelo,
        "horaEntrada": horaEntrada
    }

    print("\n" + "=" * 40)
    print("✅ VEÍCULO CADASTRADO COM SUCESSO!")
    print(f"Placa: {placa}")
    print(f"Marca: {marca}")
    print(f"Modelo: {modelo}")
    print(f"Hora de entrada: {horaEntrada}")
    print("=" * 40)

def saida_veiculo(dados):
    global total_recebido

    placa = input("Digite a placa do carro: ")

    if placa not in dados:
        print("Veículo não encontrado.")
        return
    
    horaSaida = input("Digite a hora da saida (HH:MM): ")

    horaEntrada = dados[placa]["horaEntrada"]

    horaE, minutoE = horaEntrada.split(":")
    horaS, minutoS = horaSaida.split(":")

    horaE = int(horaE)
    horaS = int(horaS)

    minutoE =int(minutoE)
    minutoS = int(minutoS)

    entradaMin = horaE * 60 + minutoE
    saidaMin = horaS * 60 + minutoS

    tempoMin = saidaMin - entradaMin

    horas = tempoMin // 60
    
    if horas < 0:
        horas +=24

    if horas <= 3:
        valor = 5
    
    else:
        horas_adicionais = horas - 3
        valor = 5 + (horas_adicionais * 2) 
    
    total_recebido += valor

    print(f"Valor a pagar: R$ {valor:.2f}")

    del dados[placa]

    print("\n" + "=" * 40)
    print("✅ VEÍCULO REMOVIDO DO ESTACIONAMENTO. OBRIGADO E VOLTE SEMPRE!")
    print(f"Placa: {placa}")
    print(f"Valor a pagar: R$ {valor:.2f}")
    print("=" * 40)
    

def listar_veiculos(dados):
    if len(dados) == 0:
        print("Nenhum veículo cadastrado.")
        return
    
    for index, placa in enumerate(sorted(dados.keys()),start=1):
        veiculo = dados[placa]
        print(
            f"{index}."
            f"Placa: {placa} | "
            f"Marca: {veiculo['marca']}  | "
            f"Modelo: {veiculo['modelo']} | "
            f"Entrada: {veiculo['horaEntrada']}"
        )

def buscar_veiculo(dados):

    placa = input("Digite o código da placa: ").upper()

    if placa in dados:

        veiculo = dados[placa]

        print(f"Veículo encontrado com sucesso!\n"
              f"Placa: {placa}\n"
              f"Marca: {veiculo['marca']}\n"
              f"Modelo: {veiculo['modelo']}\n"
              f"Hora de Entrada: {veiculo['horaEntrada']}"
        )

    else:
        print("Veículo não encontrado, tente novamente.")

dados = carregar_dados() 

op = menu()

while op != 6:
    if op == 1:
        adicionar_veiculos(dados)

    if op == 2:
        saida_veiculo(dados)
    
    if op == 3:
        listar_veiculos(dados)

    if op == 4:
        buscar_veiculo(dados)

    if op == 5:
        print(f"Total recebido no dia: R$ {total_recebido:.2f}")

    
    time.sleep(2)
    op = menu()

salvar_dados(dados)
print("\nPrograma encerrado!")