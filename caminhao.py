from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.capacidade = capacidade

moto = Caminhao("Mercedes", "Trucado", "ABC", 2001, 23000)

print(Caminhao)