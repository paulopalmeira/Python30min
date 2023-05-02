#quantos caracteres estão na variável
name = "Pedro"
print (len(name))

#Onde está um caracter 
print(name.find("o"))

#Primeira letra maiúscula
print(name.capitalize())

#Tudo maiúscula
print(name.upper())

#Tudo minúsculo
print(name.lower())

#Se for tudo número, volta True
print(name.isdigit())

#Se for tudo letra, volta True
print(name.isalpha())

print(name.count("d"))

print(name*3)
print(name.replace("d", "j"))