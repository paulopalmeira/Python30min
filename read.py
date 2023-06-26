try:
    with open('dado.txt') as file: 
        print(file.read())
except FileNotFoundError:
    print("Arquivo não existe")