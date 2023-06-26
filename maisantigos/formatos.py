# str.format()

animal = "vaca"
item = "lua"

# print("A "+animal+" foi para a "+item)

# print("A {} pulou na {}".format(animal,item))

# print("A {1} pulou na {0}".format(animal,item)) #positional argument

# print("A {animal} pulou na {item}".format(animal="vaca",item="lua"))

text = "A {} pulou na {}"

print(text.format(animal,item))

