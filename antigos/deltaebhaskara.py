import matplotlib.pyplot as plt
import math


a = int(input ("Valor de A: "))
b = int(input ("Valor de B: "))
c = int(input ("Valor de C: "))

delta = b**2 - 4*a*c

# verificando o valor do delta
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"A equação possui uma raiz real: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

# define os valores de x para o gráfico
x = range(-10, 10)

# calcula os valores de y para o gráfico
y = [a*(xi**2) + b*xi + c for xi in x]

# plota o gráfico
plt.plot(x, y)
plt.grid()

# adiciona as raízes ao gráfico
if delta >= 0:
    plt.scatter(raiz1, 0, color='red', marker='x', s=100)
if delta > 0:
    plt.scatter(raiz2, 0, color='red', marker='x', s=100)

# exibe o gráfico
plt.show()