import requests

class Usuario:
    def __init__(self, nome, sobrenome, telefone, cep):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.cep = cep
        self.endereco = self.buscarEndereco(cep)
        self.veiculosComprados = []

    def buscarEndereco(self, cep):
        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if response.status_code == 200:
                dados = response.json()
                if "erro" not in dados:
                    return f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}-{dados['uf']}"
                else:
                    return "CEP invalido"
            else:
                return "Erro ao buscar o CEP"
        except Exception as e:
            return f"Erro de conexão: {e}"

    def comprarVeiculo(self, veiculo):
        self.veiculosComprados.append(veiculo)
        print(f"Veiculo {veiculo.modelo} comprado com sucesso por {self.nome} {self.sobrenome}")

    def exibirDados(self):
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print("Veiculos comprados:")
        for v in self.veiculosComprados:
            print(f"- {v.fabricante} {v.modelo} ({v.ano})")
