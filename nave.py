##Definir as variáveis
combustivel = 100
tripulantes = []

##definir funções

def viajar():
    ##aqui vamos gastar combustível
    global combustivel ##Avisa a função que vamos identificar um variavel externa
    if (len(tripulantes) == 0):
        print("Não há tripulantes. A viagem não acontecerá! ❌")
    else:
        if(combustivel >= 30):
            combustivel = combustivel - 30
            print("A nave viajou! 🚀")
        else:
            print("Você está sem combustível suficiente. Abasteça!")
    travarMenu()

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio! ⛽")
    travarMenu()
    
def status_nave():
    ##Mostre a quantidade de combustível e os tripulantes
    print("\n------- STATUS DA NAVE -------")
    print(f"O combustível atual é {combustivel}%")
    print(f"Os tripulantes são: {tripulantes}")
    print("------------------------------- \n")
    travarMenu()

def registroTripulantes():
    ##Essa função pergunta o nome do tripulante e adiciona na lista de tripulantes
    novoTripulante = input("Qual o nome do novo tripulante?: ") #Pergunta quem
    tripulantes.append(novoTripulante) #Inserimos o novo tripulante
    print("Tripulante inserido com sucesso! 🚀")
    travarMenu()

def remover_Tripulante():
    global tripulantes
    if len(tripulantes) == 0:
        print("\nA nave não possui tripulantes. Adicione!")

    else:
        tripulantes.pop()
        print(f"\nOs tripulantes restantes são: {tripulantes}")
    travarMenu()

##Criar uma função para pausar o código entre as interações do usuário
def travarMenu():
    input("\nPressione <ENTER> para continuar....")

##Criar um menu

    print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
while True:        ##esse loop roda para sempre!
    print("\n1- Mostrar status da nave | 2- Viajar | 3-Abastecer | 4- Novo Tripulante | 5- Remover tripulante | 6- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registroTripulantes()
    elif (opcao == "5"):
        remover_Tripulante()
        
    elif (opcao == "6"):
        print("Viagem encerrada!")
        break







# status_nave()
# registroTripulantes()
# registroTripulantes()
# status_nave()


# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()