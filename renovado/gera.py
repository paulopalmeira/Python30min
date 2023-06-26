import os

path = "C:\\Users\\palmeirapa\\Documents\\pythoning\\Python30min\\dados.txt"

if os.path.exists(path):
    print("Esse caminho existe")
    if os.path.isfile(path):
        print("Esse é o arquivo")

else:
    print("O caminho não existe")