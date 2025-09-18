# importar a biblioteca pra usar a API
import requests
import copy

# criacao da classe cliente
class Cliente:
    def __init__(self, nome, sobrenome, telefone, cep, veiculosComprados):
        # definicao dos atributos
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.cep = cep
        self.endereco = self.buscarEndereco(cep)
        self.veiculosComprados = []
    
    # metodo de buscar o endereco, igual o professor nos mostrou na ultima aula
    def buscarEndereco(self, cep):
        try:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            resposta = requests.get(url)
            if resposta.status_code == 200: # deu certo a requisicao
                dados = resposta.json()
                if "erro" not in dados: 
                    return f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}-{dados['uf']}"
                else:
                    return "CEP errado"
        except Exception as e:
            return f"Erro de conexão: {e}"

    # metodo de o cliente comprar o veiculo
    def comprarVeiculo(self, veiculo):
        self.veiculosComprados.append(veiculo)
        print(f"Veiculo {veiculo.modelo} comprado com sucesso por {self.nome} {self.sobrenome}")

    # exibir os dados do cliente, e a lista de veiculos comprados (caso tenha)
    def exibirDados(self):
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print("Veiculos comprados:")
        for v in self.veiculosComprados:
            print(f"- {v.fabricante} {v.modelo} ({v.ano})")

    # Funcao de Clonar, do padrao de projeto
    def clonar(self):
        return copy.deepcopy(self)
