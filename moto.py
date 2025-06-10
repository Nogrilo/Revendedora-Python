from veiculo import Veiculo

class Moto(Veiculo):
    def __init__ (self, modelo, fabricante, cilindrada, tipoPartida, ano, cor, combustivel, valor):
        super().__init__(fabricante, modelo, cor, ano, combustivel, valor)
        self.cilindrada = cilindrada
        self.tipoPartida = tipoPartida

        print(f"a moto {self.modelo} da {self.fabricante} tem {self.cilindrada} com {self.tipoPartida} do ano {self.ano} na cor {self.cor} usa {self.combustivel} custa R${self.valor}")

    def acelerar(self):
        print("VRRRRRRROOOOMMM VRAAAP VRAAAP!")
    def freiar(self):
        print("Screeeech!")
    def buzinar(self):
        print("bip bip")

moto = Moto("Biz", "Honda", "125cc", "partida eletrica", "2008", "vermelha", "gasolina comum", "8.000,00")
moto.acelerar()
moto.freiar()
moto.buzinar()