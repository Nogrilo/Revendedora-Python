# Importar as bibliotecas e codigos

import os
from veiculo import Veiculo
from carro import Carro
from moto import Moto

# Funcoes 
# Definir a funcao de limpar a tela pra ficar bonitinho
def limpaTela():
    os.system("cls")

# Limpando a tela
limpaTela()

# Instanciando o carro
carro = Carro("Clio", "Renault", "2", "Sem", "Direção mecânica", "Branco", "2015", "Gasolina comum", "26.000,00")
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
