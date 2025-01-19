print("Bem-vindo a livraria do Vitor Filipe!")

lista_livro = []  
id_global = 0 

def cadastrar_livro(id):
    print(f"Id do livro: {id}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)
    print(f"Livro '{nome}' cadastrado com sucesso!")

def consultar_livro():
    while True:
        print("\n-----------------------------")
        print("-----Menu Consultar Livro----")
        print("-----------------------------")
        print("1. Consultar Todos os Livros")
        print("2. Consultar Livro por Id")
        print("3. Consultar Livros(s) por Autor")
        print("4. Retornar")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Consultando todos os livros:")
            if lista_livro:
                for livro in lista_livro:
                    print("\nID:", livro["id"])
                    print("Nome:", livro["nome"])
                    print("Autor:", livro["autor"])
                    print("Editora:", livro["editora"])
                    print("--------------------------")
            else:
                print("Nenhum livro cadastrado.")
        elif opcao == "2":
            id_consulta = int(input("Digite o id do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print("\nID:", livro["id"])
                    print("Nome:", livro["nome"])
                    print("Autor:", livro["autor"])
                    print("Editora:", livro["editora"])
                    print("--------------------------")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado.")
        elif opcao == "3":
            autor_consulta = input("Digite o autor do(s) livro(s): ")
            encontrado = False
            for livro in lista_livro:
                if livro["autor"].lower() == autor_consulta.lower():
                    print("\nID:", livro["id"])
                    print("Nome:", livro["nome"])
                    print("Autor:", livro["autor"])
                    print("Editora:", livro["editora"])
                    print("--------------------------")
                    encontrado = True
            if not encontrado:
                print("Livro não encontrado.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def remover_livro():
    while True:
        print("\n-----------------------------")
        print("-----Menu Remover Livro----")
        print("-----------------------------")
        id_remove = int(input("Digite o id do livro a ser removido: "))
        encontrado = False
        for livro in lista_livro:
            if livro["id"] == id_remove:
                lista_livro.remove(livro)
                print("Livro removido com sucesso!")
                encontrado = True
                break
        if encontrado:
            break
        else:
            print("Id inválido.")

while True:
    print("\n-----------------------------")
    print("-------Menu principal--------")
    print("-----------------------------")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro(s)")
    print("3. Remover Livro")
    print("4. Sair")
    opcao = input("Escolha a opção desejada:")

    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")

id_global += 1
cadastrar_livro(id_global)
id_global += 1
cadastrar_livro(id_global)
id_global += 1
cadastrar_livro(id_global)

consultar_livro()

consultar_livro()

consultar_livro()

remover_livro()
consultar_livro()
