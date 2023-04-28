# Abrindo o arquivo no modo de escrita ('w')
arquivo = open('texiste.txt', 'w')

# Escrevendo no arquivo
arquivo.write('Olá, mundo!\n')
arquivo.write('Este é um arquivo de texto criado em Python.')

# Fechando o arquivo
arquivo.close()