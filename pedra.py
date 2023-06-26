import random

escolha = ["pedra", "papel", "tesoura"]

maquina = random.choice(escolha)
jogador = None

while jogador not in escolha:
    jogador = input("Escolha: pedra, papel ou tesoura?: ").lower()

print ("A máquina escolheu: ", maquina)
print ("Você escolheu:", jogador)

