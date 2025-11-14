from veiculo import Veiculo
import copy

# Criacao da classe carro
class Caminhao(Veiculo):

    # Definicao dos atributos
    def __init__ (self, modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, capacidadeCarga, tipoCarroceria, cor, ano, combustivel, valor):
        super().__init__(fabricante, modelo, cor, ano, combustivel, valor)
        self.qttPortas          = qttPortas
        self.arCondicionado     = arCondicionado
        self.tipoDirecao        = tipoDirecao
        self.capacidadeCarga    = capacidadeCarga
        self.tipoCarroceria     = tipoCarroceria 

    # Funcao de se apresentar
    def exibirDados(self):
        print(f"Modelo: {self.modelo}\nFabricante: {self.fabricante}\nQuantidade Portas: {self.qttPortas}\nArCondicionado: {self.arCondicionado}\nCapacidadeCarga: {self.capacidadeCarga}\nTipo Carroceria: {self.tipoCarroceria}\nTipo Direcao: {self.tipoDirecao}\nCor: {self.cor}\nAno: {self.ano}\nCombustivel: {self.combustivel}\nValor: R${self.valor}\n")
        
    # Funcao de acelerar 
    def acelerar(self):
        print("VRUMMMMMM!")
    
    # Funcao de freiar
    def freiar(self):
        print("Caminhão freiando")
    
    # Funcao de buzinar
    def buzinar(self):
        print("BUBUUUU!")

    # Funcao de Clonar, do padrao de projeto
    def clonar(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"self.fabricante {self.modelo} {self.ano}"




