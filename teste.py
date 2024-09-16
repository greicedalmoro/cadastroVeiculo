from Veiculo import Veiculo
from moto import Moto

#Instanciando a classe Moto
falcon = Moto("Honda", "Falcon NX4", "abc", 2005, 400)

#Vai Imprimir o retorno do método "__str__()"
print(falcon.__str__())

#Instanciando a classe veículo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)

print(cerato.__str__())

# Abaixo estou instanciando um objeto da Classe do Veículo
meuUno = Veiculo("Fiat", "Uno", "ABC-1234", 2000)
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())


teuFusca = Veiculo("Volks", "Fusca", "DEF-1748", 1995)

#print(meuUno.calcularTempoUso())
#print(teuFusca.calcularTempoUso())

#print("")