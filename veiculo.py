from abc import ABC, abstractmethod

# Super classe/classe mae veiculo
class Veiculo(ABC):

    # Definindo os atributos do veiculo
    def __init__(self, fabricante, modelo, cor, ano, combustivel, valor):
        self.fabricante     = fabricante
        self.modelo         = modelo
        self.cor            = cor
        self.ano            = ano
        self.combustivel    = combustivel
        self.valor          = valor

    # Definindo os metodos que sao obrigatorios para todas as subclasses
    @abstractmethod
    def exibirDados(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass
    @abstractmethod
    def freiar(self):
        pass
    @abstractmethod
    def buzinar(self):
        pass

    # Definindo o metodo de clonar, do padrao de projeto Prototype
    @abstractmethod
    def clonar(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"{self.fabricante} {self.modelo} {self.ano}"

    

