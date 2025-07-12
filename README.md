# Revendedora-Python
Este projeto tem o objetivo de adicionar veiculos a uma lista, sendo:
Carro;
Caminhao;
Moto;

Ambos sendo classes filhas da classe Veiculo, onde tem seus atributos e métodos abstratos.

Nos quais são:

Atributos:
fabricante
modelo
cor
ano
combustivel
valor

Métodos:
exibirDados()
acelerar()
freiar()
buzinar()

Desenvolvemos um software bem simples, apenas com objetivo de mostrar como a Programação Orientada a Objetos funciona em Python.

E vale comentar, que no meio do projeto, decidimos fazer as funções de adicionar os veículos através dos inputs do usuário, mas acabamos
desistindo por ser algo trabalhoso, mas que seria totalmente possível.

Esperamos que goste do nosso código :) .

----

Atualização do software!

Agora temos uma nova classe, sendo o Cliente. 
Atributos:
nome
sobrenome
telefone
cep
endereco (que a API que o professor nos mostrou retorna o endereco)
veiculos comprados (lista/agregacao de veiculos comprados)

Métodos:
buscarEndereco()
comprarVeiculo()
exibirDados() 

Essa nova classe tem o diferencial de uma API integrada, que busca o endereco inserido com base no CEP.
É uma atualização bem simples, mas que utiliza uma API de terceiro, no caso viacep.

Instanciamos um cliente bem especial no nosso sistema, que compra o carro intitulado "carrao", e adiciona na lista de veiculos comprados.

Espero que goste do nosso programa!

Vinicius Miranda, Filipe e Vitor Pazda.