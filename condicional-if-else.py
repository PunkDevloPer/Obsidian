print("_______________________________")
print("verificacion de acceso")
print("_______________________________")
edad_usuario=int(input("ingresa tu edad: "))
if edad_usuario<18:
    print("no cumples la mayoria de edad")
elif edad_usuario >90:
    print("edad incorrecta")    
else:
    print("ya eres mayor de edad, puedes ingresar")
    
print("_______________________________")
nota= int(input("introduce la nota: "))
if nota<5:
    print("insuficiente")
elif nota<6:
    print("suficiente")
elif nota<7:
    print("bien")    
elif nota<9:
    print("notable")
else:
    print("sobresaliente")