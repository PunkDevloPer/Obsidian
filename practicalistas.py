"""_summary_"""
lista = [
    "maria ->valor 0",  # -> valor 0
    "pepe ",  # -> valor 1
    "martha",  # -> valor 2
    "antony"  # -> valor 3
]
print("________________________________________________________________")
print("lista[:] -> imprimir toda la lista")
print(lista[:])  # -> imprime toda la lista
print("________________________________________________________________")
print("lista[1:3] -> accede a los indices entre 1 y 3")
print(lista[1:3])  # -> accede a los indices entre 1 y 3< en este caso
print("________________________________________________________________")

print("lista[3] -> accede al indice 3 ")
print("lista[3]")  # -> accede al indice que se le indique
print("________________________________________________________________")
print("añadir un elemento al final de la lista .append(nombrelista[:])")
lista.append("juana")  # agrega un elemento al final de la lista.
print(lista[:])

print("________________________________________________________________")
print("añadir un elemento al indice que se le indique .insert(2,jose)")
lista.insert(2, "jose")  # agrega un elemento al indice que se le indique
print(lista[:])

print("________________________________________________________________")
print("extender una lista .extend([antonio, andres, lucia])")
lista.extend(["antonio", "andres", "lucia"])
print(lista[:])

print("________________________________________________________________")
print(" saber el indice de un elemento .index(antonio)")
print(lista.index("antonio"))

print("________________________________________________________________")
print("jose in lista -> saber si un elemento se encuenta en la lista funcion ")
print("jose" in lista)

print("________________________________________________________________")
print("lista.remove(andres) -> eliminar un elemento de una lista .remove(andres)")
lista.remove("andres")
print(lista[:])

print("________________________________________________________________")
print("lista.pop() -> eliminar un elemento al final de una lista .pop()")
lista.pop()
print(lista[:])
print("________________________________________________________________")
print("lista1 +lista2 -> sumar dos listas diferentes")
lista1 = ["andrew", "mark"]
lista2 = ["lina", "josua"]
lista3 = lista1+lista2
print(lista3[:])
