from veiculo import Veiculo

# Criacao da classe carro
class Carro(Veiculo):

    # Definicao dos atributos
    def __init__ (self, modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, cor, ano, combustivel, valor):
        super().__init__(fabricante, modelo, cor, ano, combustivel, valor)
        self.qttPortas      = qttPortas
        self.arCondicionado = arCondicionado
        self.tipoDirecao    = tipoDirecao

    # Funcao de acelerar 
    def acelerar(self):
        print("vraum vraum")
    
    # Funcao de freiar
    def freiar(self):
        print("som de carro freiando")
    
    # Funcao de buzinar
    def buzinar(self):
        print("biii biii")

    # Funcao de se apresentar
    def apresentar(self):
        print(f"Modelo: {self.modelo}\nFabricante: {self.fabricante}\nQuantidade Portas: {self.qttPortas}\nArCondicionado: {self.arCondicionado}\nTipo Direcao: {self.tipoDirecao}\nCor:{self.cor}\nAno: {self.ano}\nCombustivel: {self.combustivel}\nValor: R${self.valor}\n")




