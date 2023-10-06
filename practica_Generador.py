def generapares(limite):
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num=num+1
    return milista
print(generapares(10))
#Generador de numeros aleatorios

def generaPaares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvepares = generaPaares(10)
print(devuelvepares)