#Estoque
estoque = []

#Funcao de Adicionar produtos:
def adicionar():
    print("\nAdicionar ao estoque: ")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(produto)
    print(f"\n{nome} adicionado!")

#Funcao de Modificar produtos:
def modificar():
    print("\nModificar produtos do estoque: ")
    nome = input("Produto à ser atualizado: ")
    encontrado = False
    for produto in estoque:
        if produto ["nome"] == nome:
            novo_preco = float(input("Digite o preço: "))
            nova_quantidade = int(input("Nova quantidade: "))
            produto['preco'] = novo_preco
            produto['quantidade'] = nova_quantidade
            encontrado = True
            print(f"\n{nome} atualizado!")
            break
    if not encontrado:
        print(f"\n{nome} não encontrado.")


#Funcao de Visualisar produtos:
def visualisar():
    print("\nVisualisar estoque: ")
    if len (estoque) == 0:
        print("Estoque vazio")
    else:
        for produto in estoque:
            print(f"Qtd: {produto['quantidade']} - {produto['nome']} - R$ {produto['preco']:.2f}")

#Definicao de parametros:
def menu():
    while True:
        print("\n Controle de Estoque\n")
        print("1 - Adicionar um novo produto")
        print("2 - Atualizar o estoque")
        print("3 - Visualizar o estoque")
        print("4 - Desconectar")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            adicionar()
        elif opcao == '2':
            modificar()
        elif opcao == '3':
            visualisar()
        elif opcao == '4':
            print("\n Desconectando...")
            break
        else:
            print("\nErro: Por favor digite novamente:")

#Execução:
if __name__ == "__main__":
    menu()