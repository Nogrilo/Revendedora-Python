from revendedoraFacade import revendedoraFacade
import os # importar biblioteca para limpar tela

def limparTela():
    os.system('cls')

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
            limparTela()
            modelo          = input("Modelo: ")
            fabricante      = input("Fabricante: ")
            qttPortas       = int(input("Portas: "))
            arCondicionado  = input("Possui ar condicionado? (S/N): ")
            tipoDirecao     = input("Tipo direcao: ")
            cor             = input("Cor: ")
            ano             = int(input("Ano: "))
            combustivel     = input("Combustivel: ")
            valor           = float(input("Valor: "))

            facade.cadastrarCarro(modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, cor, ano, combustivel, valor)
            print("Carro cadastrado!")

        elif opcao == 2:
            limparTela()
            modelo          = input("Modelo: ")
            fabricante      = input("Fabricante: ")
            cilindrada      = int(input("Cilindrada: "))
            tipoPatida      = input("Tipo Partida: ")
            cor             = input("Cor: ")
            ano             = int(input("Ano: "))
            combustivel     = input("Combustivel: ")
            valor           = float(input("Valor: "))

            facade.cadastrarMoto(modelo, fabricante, cilindrada, tipoPatida, cor, ano, combustivel, valor)
            print("Moto cadastrada!")

        elif opcao == 3:
            limparTela()
            modelo          = input("Modelo: ")
            fabricante      = input("Fabricante: ")
            qttPortas       = int(input("Portas: "))
            arCondicionado  = input("Possui ar condicionado? (S/N): ")
            tipoDirecao     = input("Tipo direcao: ")
            capacidadeCarga = input("Capacidade Carga: ")
            tipoCarroceria  = input("Tipo da Carroceria: ")
            cor             = input("Cor: ")
            ano             = int(input("Ano: "))
            combustivel     = input("Combustivel: ")
            valor           = float(input("Valor: "))

            facade.cadastrarCaminhao(modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, capacidadeCarga, tipoCarroceria, cor, ano, combustivel, valor)
            print("Caminhao cadastrado!")

        elif opcao == 4:
            limparTela()
            nome                = input("Nome: ")
            sobrenome           = input("Sobrenome: ")
            telefone            = input("Telefone: ")
            cep                 = input("Cep: ")
            veiculosComprados   = []

            facade.cadastrarCliente(nome, sobrenome, telefone, cep, veiculosComprados)
            print("Cliente cadastrado!")

        elif opcao == 5:
            for i, v in enumerate(facade.listarVeiculos(), start=1):
                print(f"{i} - {v}")

        elif opcao == 6:
            for i, v in enumerate(facade.listarClientes(), start=1):
                print(f"{i} - {v}")

        elif opcao == 7:
            modelo              = input("Digite o modelo: ")
            nome                = input("Digite o nome do cliente: ")

            cliente = next((c for c in facade.clientes if c.nome.lower() == nome.lower()), None)

            facade.venderVeiculo(cliente, modelo)
            print("Venda concluída!")

        elif opcao == 0:
            break

main()
