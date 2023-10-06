print("becas año 2023 condicional AND")
distancia = int(input("ingrese la distancia en Km: "))
print("distancia: ", distancia)

hermanos = int(input("ingrese la cantidad de hermanos: "))  
print("cantidad de hermanos: ", hermanos)

salario=int(input("ingrese el salario: "))
print("salario: ", salario)

if distancia > 40 and hermanos>2 and salario<=20000:
    print("tienes derecho a la beca")
else:
    print("no tienes derecho a la beca")
print("_________________________________________________")

print("becas año 2023 condicional OR")
distancia = int(input("ingrese la distancia en Km: "))
print("distancia: ", distancia)

hermanos = int(input("ingrese la cantidad de hermanos: "))  
print("cantidad de hermanos: ", hermanos)

salario=int(input("ingrese el salario: "))
print("salario: ", salario)

if distancia > 40 and hermanos>2 or salario<=20000:
    print("tienes derecho a la beca")
else:
    print("no tienes derecho a la beca")
print("_______________________________________________")

print("asignaturas optativas 2023 condicional IN")
print("informatica grafica -pruebas de software -usabilidad y accesibilidad")
asignatura = input("ingrese la asignatura: ")
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("tienes derecho a la asignatura", asignatura)
else:
    print("no tienes derecho a la asignatura", asignatura)