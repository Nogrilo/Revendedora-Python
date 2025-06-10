from veiculo import Veiculo

# Criacao da classe moto
class Moto(Veiculo):

    # Definicao dos atributos
    def __init__ (self, modelo, fabricante, cilindrada, tipoPartida, ano, cor, combustivel, valor):
        super().__init__(fabricante, modelo, cor, ano, combustivel, valor)
        self.cilindrada     = cilindrada
        self.tipoPartida    = tipoPartida

        print(f"a moto {self.modelo} da {self.fabricante} tem {self.cilindrada} com {self.tipoPartida} do ano {self.ano} na cor {self.cor} usa {self.combustivel} custa R${self.valor}")

    # Funcao de acelerar bem barulhento
    def acelerar(self):
        print("VRRRRRRROOOOMMM VRAAAP VRAAAP!")
    
    # Funcao de freiar
    def freiar(self):
        print("Screeeech!")

    # Funcao de buzinar bem baixinho
    def buzinar(self):
        print("bip bip")

    # Funcao de apresentar 
    def apresentar(self):
        print(f"Modelo: {self.modelo}\nFabricante: {self.fabricante}\nCilindrada: {self.cilindrada}\nTipo Partida: {self.tipoPartida}\nAno: {self.ano}\nCor: {self.cor}\nCombustivel: {self.combustivel}\nValor: R${self.valor}")
