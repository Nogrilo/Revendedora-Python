# Importar as bibliotecas e codigos

import os
from veiculo import Veiculo
from carro import Carro
from moto import Moto
from caminhao import Caminhao

# Funcoes 
# Definir a funcao de limpar a tela pra ficar bonitinho
def limpaTela():
    os.system("cls")

# Limpando a tela
limpaTela()

# Instanciando o carro
carro = Carro("Clio", "Renault", 2, "Não", "Direção mecânica", "Branco", "2015", "Gasolina comum", "26.000,00")
carro.apresentar()
carro.acelerar()
carro.freiar()
carro.buzinar()

# Instanciando a moto
moto = Moto("Biz", "Honda", "125cc", "Elétrica", "2008", "Vermelha", "Gasolina comum", "8.000,00")
moto.apresentar()
moto.acelerar()
moto.freiar()
moto.buzinar()

# Instanciando o caminhao
caminhao = Caminhao("Grande","Scania", 2,"Sim", "Elétrica", "35T", "Baú 4 Eixos", "Bordô", "2025", "Diesel", "1.000.000.00")
caminhao.apresentar()
caminhao.acelerar()
caminhao.freiar()
caminhao.buzinar()


