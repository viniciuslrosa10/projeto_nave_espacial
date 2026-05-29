##Definir as variáveis
combustivel = 100
tripulantes = []

##definir funções

def viajar():
    ##aqui vamos gastar combustível
    global combustivel ##Avisa a função que vamos identificar um variavel externa
    if(combustivel >= 30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustível suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio! ⛽")
    
def status_nave():
    ##Mostre a quantidade de combustível e os tripulantes
    print("\n------- STATUS DA NAVE -------")
    print(f"O combustível atual é {combustivel}%")
    print(f"Os tripulantes são: {tripulantes}")
    print("------------------------------- \n")

def registroTripulantes():
    ##Essa função pergunta o nome do tripulante e adiciona na lista de tripulantes
    novoTripulante = input("Qual o nome do novo trpulante?: ") #Pergunta quem
    tripulantes.append(novoTripulante) #Inserimos o novo tripulante
    print("Tripulante inserido com sucesso! 🚀")


##Criar um menu

    print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
while True:        ##esse loop roda para sempre!
    print("\n1- Mostrar status da nave | 2- Viajar | 3-Abastecer | 4- Novo Tripulante | 5- Sair")
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