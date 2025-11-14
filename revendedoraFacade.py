from carro import Carro
from moto import Moto
from caminhao import Caminhao
from cliente import Cliente

class revendedoraFacade:
    def __init__(self):
        self.veiculos = []
        self.clientes = []

    def cadastrarCliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
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

    def cadastrarCaminhao(self, marca, modelo, ano, preco, eixo):
        caminhao = Caminhao(marca, modelo, ano, preco, eixo)
        self.veiculos.append(caminhao)
        return caminhao

    def listarVeiculos(self):
        return self.veiculos

    def venderVeiculo(self, cliente, id_veiculo):
        if id_veiculo < 0 or id_veiculo >= len(self.veiculos):
            return None
        
        veiculo = self.veiculos[id_veiculo]
        cliente.adicionar_compra(veiculo)
        self.veiculos.pop(id_veiculo)
        return veiculo
