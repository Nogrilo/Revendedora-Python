from carro import Carro
from moto import Moto
from caminhao import Caminhao
from cliente import Cliente

class revendedoraFacade:
    def __init__(self):
        self.veiculos = []
        self.clientes = []

    def cadastrarCliente(self, nome, sobrenome, telefone, cep, veiculosComprados):
        cliente = Cliente(nome, sobrenome, telefone, cep, veiculosComprados)
        self.clientes.append(cliente)
        return cliente

    def listarClientes(self):
        return self.clientes

    def cadastrarCarro(self, modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, cor, ano, combustivel, valor):
        carro = Carro(modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, cor, ano, combustivel, valor)
        self.veiculos.append(carro)
        return carro

    def cadastrarMoto(self, modelo, fabricante, cilindrada, tipoPartida, ano, cor, combustivel, valor):
        moto = Moto(modelo, fabricante, cilindrada, tipoPartida, ano, cor, combustivel, valor)
        self.veiculos.append(moto)
        return moto

    def cadastrarCaminhao(self, modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, capacidadeCarga, tipoCarroceria, cor, ano, combustivel, valor):
        caminhao = Caminhao(modelo, fabricante, qttPortas, arCondicionado, tipoDirecao, capacidadeCarga, tipoCarroceria, cor, ano, combustivel, valor)
        self.veiculos.append(caminhao)
        return caminhao

    def listarVeiculos(self):
        return self.veiculos

    def venderVeiculo(self, cliente, modelo):
        veiculo = self.buscarVeiculoPorModelo(modelo)

        cliente.comprarVeiculo(veiculo)

        self.veiculos.remove(veiculo)

    # metodo para buscar o veiculo dentro da lista
    def buscarVeiculoPorModelo(self, modelo):
        for v in self.veiculos:
            if v.modelo.lower() == modelo.lower():
                return v
        return None
