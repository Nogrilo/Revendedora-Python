from veiculo import Veiculo
import copy

# Criacao da classe moto
class Moto(Veiculo):

    # Definicao dos atributos
    def __init__ (self, modelo, fabricante, cilindrada, tipoPartida, ano, cor, combustivel, valor):
        super().__init__(fabricante, modelo, cor, ano, combustivel, valor)
        self.cilindrada     = cilindrada
        self.tipoPartida    = tipoPartida


    # Funcao de apresentar 
    def exibirDados(self):
        print(f"Modelo: {self.modelo}\nFabricante: {self.fabricante}\nCilindrada: {self.cilindrada}\nTipo Partida: {self.tipoPartida}\nAno: {self.ano}\nCor: {self.cor}\nCombustivel: {self.combustivel}\nValor: R${self.valor}")

    # Funcao de acelerar bem barulhento
    def acelerar(self):
        print("VRRRRRRROOOOMMM VRAAAP VRAAAP!")
    
    # Funcao de freiar
    def freiar(self):
        print("Screeeech!")

    # Funcao de buzinar bem baixinho
    def buzinar(self):
        print("bip bip")

    # Funcao de Clonar, do padrao de projeto
    def clonar(self):
        return copy.deepcopy(self)
