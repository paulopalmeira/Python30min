# exceptions

try:
    numerador = int(input("Insira um número para dividir: "))
    denominador = int(input("Insira um número para ser divisor: "))
    resultado = numerador / denominador
    print(resultado)
except ZeroDivisionError:
    print("Não pode dividir por zero")
except ValueError:
    print("Digite apenas números")



#except Exception:
#    print("Alguma coisa errada!")