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
        
dados = carregar_dados()

op = menu()

while op != 6:
    # falta as funções de Vitoria e Aleckson




    op = menu()

salvar_dados(dados)