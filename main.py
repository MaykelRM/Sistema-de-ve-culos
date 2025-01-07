from veiculos import Veiculos


def cadastro_veiculo(_veiculos):
    tipo = input("Carro ou moto: ")
    marca = input("Qual a marca: ")
    modelo = input("Qual o modelo: ")
    ano = int(input("Qual o ano do veículo: "))
    chassi = input("Qual o código do chassi: ")
    cap_tanq = float(input("Capacidade do tanque (litros): "))
    cons_medio = float(input("Consumo médio (km/l): "))
    info_extra = input("Informação extra: ")

    _veiculos[chassi] = Veiculos(marca, modelo, ano, tipo, info_extra, cap_tanq, cons_medio, chassi)
    print("Veículo cadastrado com sucesso")

def excluir(_veiculos):
    chassi = input("Digite o código do chassi: ")
    if chassi in _veiculos:
        del _veiculos[chassi]
        print("Veículo excluído com sucesso.")
    else:
        print("Chassi não encontrado.")

def exibir_chassis(_veiculos):
    if _veiculos:
        print("Chassis cadastrados:")
        for chassi in _veiculos.keys():
            print(chassi)
    else:
        print("Nenhum chassi cadastrado.")

def info(_veiculos):
    if _veiculos:
        print("--- Veículos cadastrados ---")
        for chassi in _veiculos:
            _veiculos[chassi].exibir_detalhes()
    else:
        print("Nenhum veículo cadastrado.")

def main():
    _veiculos = {}

    while True:
        print("\n1. Cadastrar veículo")
        print("2. Excluir cadastro de veículo")
        print("3. Exibir todos os chassis cadastrados")
        print("4. Exibir informações do veículo")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastro_veiculo(_veiculos)
        elif opcao == 2:
            excluir(_veiculos)
        elif opcao == 3:
            exibir_chassis(_veiculos)
        elif opcao == 4:
            info(_veiculos)
        elif opcao == 5:
            print("Saíndo do sistema")
            break
        else:
            print("Opção inválida. Tente novamente")
main()

