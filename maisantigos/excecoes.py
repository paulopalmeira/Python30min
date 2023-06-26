# exceptions

try:
    numerador = int(input("Insira um número para dividir: "))
    denominador = int(input("Insira um número para ser divisor: "))
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(e)
    print("Não pode dividir por zero")
except ValueError as e:
    print(e)
    print("Digite apenas números")
except Exception as e:
    print(e)
    print("Tem alguma coisa errada")
else:
    print(resultado)
finally:
    print("Isso aqui vai ser executado em qualquer dos casos")



#except Exception:
#    print("Alguma coisa errada!")