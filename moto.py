from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas

    #Override - Subscrever o método __str__()
    def __str__(self):
        ret = super ().__str__()
        return f'''{ret}
        - Cilindradas: {self.__cilindradas}'''