print("----- SEJA BEM-VINDO AO SISTEMA DE ESTOQUE -----")
produto = [
    ["GT23","Parafuso",203,56],
    ["BL67","Porca",421,98],
    ["FGH83","Prego",896,76]
]

def adicionar_produtos():
    global produto
    idProduto= (input("Qual o ID do produto?:"))
    nomeProduto= input("Qual o nome do produto?:")
    quantidadeProduto= (input("Qual a quantidadeb disponível no estoque?:"))
    posiçãoProduto= (input("Qual a sua posição?:"))

    novo_produto = [idProduto, nomeProduto, quantidadeProduto,posiçãoProduto]

    produto.append(novo_produto)
    print("Produto adicionado com sucesso!")
    adicionar_produtos()


#3 [id.nome,quantidade,localização]
#