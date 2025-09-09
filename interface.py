# Importar as bibliotecas e codigos

import os
from veiculo import Veiculo
from carro import Carro
from moto import Moto
from caminhao import Caminhao
from cliente import Cliente

# Funcoes 
# Definir a funcao de limpar a tela pra ficar bonitinho
def limpaTela():
    os.system("cls")

# Funcao de adicionar carro
#def adicionarCarro():
#    print("==== Cadastro de Carro ====")
#    modelo = input("Modelo: ")
#    fabricante = input("Fabricante: ")
#    qtt_portas = int(input("Quantidade de portas: "))
#    ar_condicionado = input("Tem ar condicionado (Sim/Não): ").strip().lower() == "sim"
#    tipo_direcao = input("Tipo de direção: ")
#    cor = input("Cor: ")
#    ano = input("Ano: ")
#    combustivel = input("Combustível: ")
#    valor = input("Valor: ")
#
#    carro = Carro(modelo, fabricante, qtt_portas, ar_condicionado, tipo_direcao, cor, ano, combustivel, valor)
#    return carro

# Funcao de adicionar moto
#def adicionarMoto():
#    print("==== Cadastro de Moto ====")
#    modelo = input("Modelo: ")
#    fabricante = input("Fabricante: ")
#    cilindrada = input("Quantidade de cilindrada: ")
#    tipoPartida = input("Tipo da Partida: ")
#    cor = input("Cor: ")
#    ano = input("Ano: ")
#    combustivel = input("Combustível: ")
#   valor = input("Valor: ")
#
#    moto = Moto(modelo, fabricante, cilindrada, tipoPartida, cor, ano, combustivel, valor)
#    moto.apresentar()


# Limpando a tela
limpaTela()


# Instanciando o carro
#carro = Carro("Clio", "Renault", 2, "Não", "Direção mecânica", "Branco", "2015", "Gasolina comum", "26.000,00")


# Instanciando a moto
#moto = Moto("Biz", "Honda", "125cc", "Elétrica", "2008", "Vermelha", "Gasolina comum", "8.000,00")


# Instanciando o caminhao
#caminhao = Caminhao("Grande","Scania", 2,"Sim", "Elétrica", "35T", "Baú 4 Eixos", "Bordô", "2025", "Diesel", "1.000.000.00")


# Instanciando o carrao que o cliente irá comprar
#carrao = Carro("Civic", "Honda", 4, "Sim", "Direção elétrica", "Cinza escuro", "2025", "Flex", "120.000")

# Criar lista de veiculos
#veiculos = [carro, moto, caminhao, carrao]

# Mostrar todos os dados dos veiculos
#for veiculo in veiculos:
#    veiculo.exibirDados()
#    print("\n")

# Instanciando o cliente numero 1 do software :)
#cliente = Cliente("Professor Carlos", "Guerber", "47 9 9999-9999", "89464024")

# Exibir os dados
#cliente.exibirDados()

# Comprar o carrao
#cliente.comprarVeiculo(carrao)

# Exibir os dados, agora com a compra de um veiculo
#cliente.exibirDados()

carro01 = Carro("Civic", "Honda", 4, "Sim", "Direção Elétrica", "Preto", "2025", "Flex", "120.000")
carro02 = carro01.clone()

carro01.exibirDados()
carro02.exibirDados()


