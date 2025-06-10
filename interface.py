# Importar as bibliotecas e codigos

from veiculo import Veiculo
from carro import Carro
from moto import Moto

# Instanciando o carro

carro = Carro("clio", "renaut", "2 portas", "sem ar", "direção mecanica", "branco", "2015", "gasolina comum", "26.000,00")
carro.apresentar()
carro.acelerar()
carro.freiar()
carro.buzinar()

# Instanciando a moto

moto = Moto("Biz", "Honda", "125cc", "partida eletrica", "2008", "vermelha", "gasolina comum", "8.000,00")
moto.acelerar()
moto.freiar()
moto.buzinar()