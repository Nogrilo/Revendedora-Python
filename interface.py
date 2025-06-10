# Importar as bibliotecas e codigos

import os
from veiculo import Veiculo
from carro import Carro
from moto import Moto

# Funcoes 
def limpaTela():
    os.system("cls")

# Limpando a tela
limpaTela()

# Instanciando o carro

carro = Carro("clio", "renaut", "2 portas", "sem ar", "direção mecanica", "branco", "2015", "gasolina comum", "26.000,00")
carro.apresentar()
carro.acelerar()
carro.freiar()
carro.buzinar()

# Instanciando a moto

moto = Moto("Biz", "Honda", "125cc", "partida eletrica", "2008", "vermelha", "gasolina comum", "8.000,00")
moto.apresentar()
moto.acelerar()
moto.freiar()
moto.buzinar()

# Definir a funcao de limpar a tela pra ficar bonitinho
