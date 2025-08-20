import os

os.system

print("Hola Soy Tu asistente del Clima")

dinero= int(input("Ingresa tu presupuesto (1000 - 50000) "))

print("1. Soleado")
print("2. Lluvioso")
print("3. Nublado")
print("4. Nevado")
opcion= int(input("Ingresa la Opcion que contenga tu clima actual "))

if (opcion==1 and dinero >= 50000):
    
    print("En un dia Soleado Te recomiendo Un Brunch")
    
elif (opcion==1 and dinero < 50000):
    
    print("En un dia Soleado Te recomiendo Un pasadia")
    
elif (opcion==2 and dinero >= 50000 ):
    print("En un dia Lluvioso Pedir comida a domicilio")
    
elif (opcion==2 and dinero < 50000 ):
    print("En un dia Lluvioso Te recomiendo rentar una pelicula")
    
elif(opcion==3 and dinero >= 50000):
    print("En un dia Nublado Te recomiendo comprar un videojuego nuevo")
    
elif (opcion==3 and dinero < 50000 ):
    print("En un dia Nublado Te recomiendo leer un libro")
    
elif(opcion==4 and dinero >= 50000):
    print("En un dia Nevado te recomiendo salir a esquiar")
    
elif (opcion==4 and dinero < 50000 ):
    print("En un dia Nevado Te recomiendo comprar un chocolate caliente")
    
else:
    
    print("Ingrese una opcion valida")
