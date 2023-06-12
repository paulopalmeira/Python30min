# scope
# escopo GLOBAL e escopo LOCAL

nome = "Maria"

def mostra_o_nome():
    nome = "Paulo"     # escopo LOCAL (disponível
    print(nome)        # somente dentro da função)

mostra_o_nome()
print(nome)
