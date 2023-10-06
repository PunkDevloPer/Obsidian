print("bucle determinado for")
print("la estructura es -> for in elemento a recorrer:  ")
for i in [1, 2, 3]:
    print("hola mundo")

print("fin del bucle")
for estaciones in ["primavera", "verano", "otoño", "invierno"]:
    print(estaciones)

for nombres in ["juan", "pedro", "maria", "luis"]:
    print(nombres)

for i in ["pildoras", "informaticas", "diseñadoras"]:
    print(i)

count = 0
email = input("ingrese su email: ")
for i in email:
    if (i == "@" or i == "."):
        count = count + 1
if (count == 2):
    print("email correcto")
else:
    print("email incorrecto")

print("fin del bucle")

# for i in range(5):
#    print(i)
# una modificacion al archivo del bucle for
