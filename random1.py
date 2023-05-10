import random

# Gera um número inteiro aleatório entre 1 e 100 (inclusive)
numero_aleatorio = random.randint(1, 100)

# Gera um número decimal aleatório entre 0 e 1
numero_decimal_aleatorio = random.random()

# Gera um número decimal aleatório entre 1 e 10 com 2 casas decimais
numero_decimal_aleatorio_preciso = round(random.uniform(1, 10), 2)

print(numero_aleatorio)
print(numero_decimal_aleatorio)
print(numero_decimal_aleatorio_preciso)