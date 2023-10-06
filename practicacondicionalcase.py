salario_presidente= int(input("digite un salario de presidente: "))
print("el salario del presidente es: ",salario_presidente)

salario_director= int(input("digite un salario de director: "))
print("el salario del director es: ",salario_director)

salario_jefe_area= int(input("digite un salario de jefe de area: "))
print("el salario del jefe de area es: ",salario_jefe_area)

salario_administrativo= int(input("digite un salario administrativo: "))
print("el salario administrativo es: ",salario_administrativo)
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("todo funciona de forma correcta en la empresa")
else:
    print("algo no esta funcionando en la empresa")