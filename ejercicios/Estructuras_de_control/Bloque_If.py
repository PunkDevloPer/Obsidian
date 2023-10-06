"""Bloque If que pregunta la edad de una persona y si es mayor de edad imprime un mensaje"""

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")


# bloque if que pregunta un numero y si es par imprime un mensaje:
num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("El numero es par")
