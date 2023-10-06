def evaluacion(nota): #recibe la variable nota
    valoracion="aprobado" # definimos la primera variable
    if nota<5: #si nota es menor a 5 entonces esta desaprobado de lo contrario esta aprobado.
        valoracion="desaprobado"
    return valoracion
print(evaluacion(1))