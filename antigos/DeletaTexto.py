# Abrir o arquivo original e ler todo o conteúdo em uma lista
with open('texiste.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Mostra o conteúdo original
print (linhas)

# Excluir a segunda linha (índice 1) da lista
del linhas[1]

# Escrever o conteúdo atualizado de volta no arquivo
with open('texiste.txt', 'w') as arquivo:
    for linha in linhas:
        arquivo.write(linha)

# Mostra o conteúdo após a rotina de exclusão
print (linhas)