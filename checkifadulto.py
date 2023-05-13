idade = int(input("Digite sua idade: "))


if idade == 100:
    print("Você é centenário")
elif idade >= 18:
    print("Você é adulto")
elif idade < 0:
    print("Você nem nasceu")
else:
    print("Você é menor de idade")
