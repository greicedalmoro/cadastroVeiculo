from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas

moto = Moto("Honda", "Falcon NX4", "ABC", 2005, 400)

print(moto)