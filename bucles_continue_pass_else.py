for letra in "python":
    if letra == "h":
        continue  # salta al siguiente bucle y salta a la siguiente linea de codigo
    print("la letra es", letra)

nombre = "pildoras informaticas"
contador = 0
print(len(nombre))  # cuenta la cantidad de caracteres

for i in nombre:
    if i == " ":
        continue  # salta al siguiente bucle y salta a la siguiente linea de codigo
    contador += 1
print(contador)
