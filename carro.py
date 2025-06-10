from veiculo import Veiculo

class Carro(Veiculo):
    def __init__ (self, modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, cor, ano, combustivel, valor):
        super().__init__(fabricante, modelo, cor, ano, combustivel, valor)

        self.qttPortas = qttPortas
        self.arCondicionado = arCondicionado
        self.tipoDirecao = tipoDirecao

        print(f"O {self.modelo} da {self.fabricante} tem {self.qttPortas}, {self.arCondicionado}, {self.tipoDirecao} da cor {self.cor} ano {self.ano} combustivel {self.combustivel} e custa R${self.valor}")

    def acelerar(self):
        print("vraum vraum")
    def freiar(self):
        print("som de carro freiando")
    def buzinar(self):
        print("biii biii")

carro = Carro("clio", "renaut", "2 portas", "sem ar", "direção mecanica", "branco", "2015", "gasolina comum", "26.000,00")
carro.acelerar()
carro.freiar()
carro.buzinar()

