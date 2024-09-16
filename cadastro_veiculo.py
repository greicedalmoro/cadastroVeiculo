import os
os.system('clear')

from carro import Carro
from moto import Moto
from Veiculo import Veiculo
from caminhao import Caminhao

#BD em memória
listaVeiculos =[]

def cadastrar():
    os.system('clear')
    print("Qual o tipo de veículo: (1) Carro - (2) Moto - (3) Caminhão")
    tipo = input()
    print("Digite a marca: ")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite a placa:")
    placa = input().strip().upper()
    print("Digite o ano")
    ano = input()

    if tipo == "1":
        nPortas =  input("Digite o número de portas: ")
        veiculoAdd = Carro(marca, modelo, placa, ano, nPortas)
    elif tipo == "2":
        cilindradas = input("Digite as cilindradas: ")
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
    elif tipo == "3":
        capacidade = input("Digite a capacidade: ")
        veiculoAdd = Caminhao(marca, modelo, placa, ano, capacidade)
    listaVeiculos.append(veiculoAdd)

def listar():
    os.system('clear')
    if len(listaVeiculos) == 0:
        print ("Não existem veículos cadastrados.")  
    else:
        i = 1
        for veiculo in listaVeiculos:
            print(f"Veículos: {i}")
            print(f"{veiculo}")
            i +=1
    print()
    input("Pressione Enter para continuar...")
              
def excluir():
    listar()
    print("Digite a placa que deseja excluir:")
    placa = input().strip().upper()
    encontrou = False 
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("Veículo excluído")
    else:
        print("Veículo não encontrado")
    
    print()
    input("Pressione Enter para continuar...")            
    


while True:
    os.system('clear')
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículo")
    print("0 - SAIR")

    opcao = input()
    try:
        opcao = int(opcao)
    except ValueError:
        print("Opção Inválida")
        continue

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")

        print()
        input("Pressione Enter para continuar...")
