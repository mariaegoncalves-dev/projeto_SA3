print("----- SEJA BEM-VINDO AO SISTEMA DE ESTOQUE 🪚🛠️⚒️ -----")
def travarmenu():
    input("\nPressione <ENTER> para abrir o menu interativo...")

produto = [
    [423,"Parafuso 🔩",203,56],
    [767,"Porca 🔩",421,98],
    [283,"Prego 🔩",896,76]
]

def adicionar_produtos():
    global produto
    id_Produto= (input("Qual o ID do produto?:"))
    nome_Produto= input("Qual o nome do produto?:")
    quantidade_Produto= (input("Qual a quantidade disponível no estoque?:"))
    posição_Produto= (input("Qual a sua posição?:"))

    novo_produto = [id_Produto, nome_Produto, quantidade_Produto,posição_Produto]

    produto.append(novo_produto)
    print("Produto adicionado com sucesso!🎉")
    
## DEFININDO FUNÇÕES

def adicionar_produtos():
    novoProduto = input("Qual o nome do novo produto?:") 
    produto.append(novoProduto) 
    print("Produto adicionado com sucesso!🎉")
    travarmenu()

def listar_Produto():
   print("\n ----- MOSTRANDO PRODUTOS DO ESTOQUE -----")
   for linha in produto:
       print(linha)
   travarmenu()
   
def buscarId_Produto():
    global produto
    id_Produto= int(input("Qual o ID do produto?:"))
    linhaProcurada = -1
    for i in range(len(produto)): 
        if(produto[i][0] == id_Produto): 
            linhaProcurada = i 
            break
    if linhaProcurada != -1:
        print(f"O produto procurado é: {produto[linhaProcurada]}")
    
    else:
        print("O produto com esse ID não foi encontrado, insira um válido!❌")
    travarmenu()

def atualizar_Produto():
    global produto
    buscarId_Produto =int(input("Qual o ID do produto que você quer atualizar?"))
    linhaProcurada = -1 
    for i in range(len(produto)): 
    
        if(produto[i][0] == buscarId_Produto): 
            linhaProcurada = i 
  
    if linhaProcurada != -1:
        print(f"\nProduto encontrado: {produto[linhaProcurada]}")
        nova_qant = int(input("Qual a nova quantidade do produto?"))
        produto[linhaProcurada] 
        print("Quantidade atualizada com sucesso! 🎉")
    else:
        print(" Não foi possível achar o ID desse produto ❌")
    travarmenu()


### CRIANDO O MENU 
print("\n---- MENU INTERATIVO 🖥️----")
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
        print("Saindo do menu interativo")
        break

