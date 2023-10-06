""""" if condicion:
            ejecuta el codigo dentro del if
        else:
            ejecuta el codigo dentro del else
"""
#ejemplo de condicion if

print(5*"#","ejemplo de condicional if",5*"#")

color= "rojo"
if color=="rojo":
    print("el color es rojo")
else:
    print("el color no es rojo")
    
#pero si cambiamos el color a verde, no se ejecutara el codigo, sino que se ejecutara el else
color= "verde"
if color=="rojo":
    print("el color es rojo")
else:
    print("el color no es rojo")

#ahora podemos usar el input para pedirle al usuario que ingrese un color

#creamos una variable
color = input("adivina mi color favorito: ")

if color == "azul":
    print("Felicidades, adivinaste mi color favorito")
else:
    print("Lo siento, no adivinaste mi color favorito")
    
edad = int(input("ingresa tu edad: "))
if edad >=18:
    print(" ponte a chambear prro")
else:
    print("estudia programacion prro")