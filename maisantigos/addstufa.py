# *ARGS

def adiciona(*stuff):
    soma = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        soma += i
    return soma

print(adiciona(1,2,3,4,5,6))