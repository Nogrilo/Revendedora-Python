from revendedoraFacade import revendedoraFacade

def main():
    facade = revendedoraFacade()

    while True:
        print("\n1 - Cadastrar Carro")
        print("2 - Cadastrar Moto")
        print("3 - Cadastrar Caminhão")
        print("4 - Cadastrar Cliente")
        print("5 - Listar Veículos")
        print("6 - Listar Clientes")
        print("7 - Vender Veículo")
        print("0 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:
            modelo          = input("Modelo: ")
            fabricante      = input("Fabricante: ")
            qttPortas       = int(input("Portas: "))
            arCondicionado  = input("Possui ar condicionado? (S/N): ")
            tipoDirecao     = input("Tipo direcao: ")
            cor             = input("Cor: ")
            ano             = int(input("Ano: "))
            combustivel     = input("Combustivel: ")
            valor           = float(input("Valor: "))

            facade.cadastrar_carro(modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, cor, ano, combustivel, valor)
            print("Carro cadastrado!")

        elif opcao == 5:
            for i, v in enumerate(facade.listar_veiculos()):
                print(f"{i} - {v}")

        elif opcao == 7:
            id = int(input("ID do veículo: "))
            cpf = input("CPF do cliente: ")

            cliente = next((c for c in facade.clientes if c.cpf == cpf), None)

            if cliente:
                facade.vender_veiculo(cliente, id)
                print("Venda concluída!")

        elif opcao == 0:
            break

main()
