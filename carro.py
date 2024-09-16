from Veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, nPortas):
        super().__init__(marca, modelo, placa, ano)
        self.__nPortas = nPortas

    #Override - Subscrever o método __str__()
    def __str__(self):
        ret = super ().__str__()
        return f'''{ret}
    - Num. Portas: {self.__nPortas}'''