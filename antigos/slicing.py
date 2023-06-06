#Extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "Paulo Palmeira"

first_name = name[0:5]
last_name = name[6:15]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# se deixar em branco o start [:y:z] ele entende 0
# se deixar em branco o stop [x::z] ele entende o last
# se deixar em branco o step [x:y:] ele não pula nada

# AGORA, vamos falar de SLICE:

website1 = "http://google.com"
website2 = "http://wikipedia.com"

my_slice = slice(7,-4)

print(website1[my_slice])
print(website2[my_slice])

#esse -4 é contando de trás pra frente