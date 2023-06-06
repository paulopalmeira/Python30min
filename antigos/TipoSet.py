# set = coleção desordenada

nomes = {"Alice", "Bob", "Charlie"}  # Conjunto inicial de nomes

nome = input("Digite um nome: ")

opcao = input("Deseja adicionar ou remover o nome? (Digite 'adicionar' ou 'remover'): ")

if opcao == "adicionar":
    if nome in nomes:
        print(f"O nome '{nome}' já existe no conjunto.")
    else:
        nomes.add(nome)
        print(f"O nome '{nome}' foi adicionado ao conjunto.")
elif opcao == "remover":
    if nome in nomes:
        nomes.remove(nome)
        print(f"O nome '{nome}' foi removido do conjunto.")
    else:
        print(f"O nome '{nome}' não existe no conjunto.")
else:
    print("Opção inválida!")

print(nomes)  # Exibe o conjunto atualizado após a adição ou remoção (ou sem alterações)
