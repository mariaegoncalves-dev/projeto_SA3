print("----- SEJA BEM-VINDO AO SISTEMA DE ESTOQUE -----")
produto = [
    ["GT23","Parafuso",203,56],
    ["BL67","Porca",421,98],
    ["FGH83","Prego",896,76]
]

def adicionar_produtos():
    global produto
    id_Produto= (input("Qual o ID do produto?:"))
    nome_Produto= input("Qual o nome do produto?:")
    quantidade_Produto= (input("Qual a quantidadeb disponível no estoque?:"))
    posição_Produto= (input("Qual a sua posição?:"))

    novo_produto = [id_Produto, nome_Produto, quantidade_Produto,posição_Produto]

    produto.append(novo_produto)
    print("Produto adicionado com sucesso!")
    
## DEFINIR FUNÇÕES

def adicionar_produtos():
    novoProduto = input("Qual o nome do novo tripulante?:") # Pergunta quem 
    produto.append(novoProduto) # Inserir fulano
    print("Produto adicionado com sucesso!")

def listar_Produto():
   print("\n ----- MOSTRANDO PRODUTOS DO ESTOQUE -----")
   print(f"Os produtos presentes no estoque são: {produto}")

def buscarId_Produto():
    id_Produto= int(input("Qual o ID do produto?:"))
    linhaProcurada = -1
for i in range(len(produto)): #Varre a linha a linha na matriz
    if(produto[i][0] == buscarId_Produto): ## VERIFICAR SE A POSIÇÃO DO NOME É IGUAL AO NOME PROCURADO 
        linhaProcurada = i 
print(f"O produto procurado é: produto {produto[linhaProcurada]}")

def atualizar_Produto():
    global produto
print("Qual o ID do produto que você quer atualizar?")

### CRIANDO O MENU 
print("---- MENU INTERATIVO ----")
while True:
    print("Bem vindo ao menu interativo do estoque. Por favor selecione uma opção:")
    print("\n1- adicionar_Produto | 2 - listar_Produto | 3- buscarID_Produto | 4- atualizar_Produto | 5- sair ")
    opção = input("Escolha:") 
    if (opção == "1"):
        adicionar_produtos()
    elif (opção == "2"):
        listar_Produto()
    elif (opção == "3"):
        buscarId_Produto()
    elif (opção == "4"):
         atualizar_Produto()
    elif(opção == "5"):
        break
    print("Saindo do menu interativo!")

    

