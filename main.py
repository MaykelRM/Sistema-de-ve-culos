from veiculos import Veiculos

def main():
    veiculos = []

    while True:
        print("\n1. Cadastrar veículo")
        print("2. Exibir todos os veículos")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tipo = input("Carro ou moto: ")
            marca = input("Qual a marca: ")
            modelo = input("Qual o modelo: ")
            ano = int(input("Qual o ano do veículo: "))
            cap_tanq = float(input("Capacidade do tanque (litros): "))
            cons_medio = float(input("Consumo médio (km/l): "))
            info_extra = input("Informação extra: ")

            _veiculos = Veiculos(marca, modelo, ano, tipo, info_extra, cap_tanq, cons_medio)
            veiculos.append(_veiculos)
            print("Veículo cadastrado com sucesso")

        elif opcao == 2:
            if veiculos:
                print("---Veículos---")
                for _veiculos in veiculos:
                    _veiculos.exibir_detalhes()
            else:
                print("Nenhum veículo cadastrado")

        elif opcao == 3:
            print("Saíndo do sistema")
            break
        else:
            print("Opção inválida. Tente novamente")
main()

