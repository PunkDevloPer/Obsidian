"""System module."""
import math
print("Programa de calculo de raiz cuadrada")
numero = int(input("ingrese un numero: "))
Attempts = 0
while numero < 0:
    print("ingrese un numero positivo")
    if Attempts == 2:
        print("has realizado demasiados intentos")
        break
    numero = int(input("ingrese un numero: "))
    if numero < 0:
        Attempts = Attempts + 1
if Attempts < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de ", numero, "es", solucion)
