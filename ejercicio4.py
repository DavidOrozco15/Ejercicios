import os

os.system

print("Hola")
nota=int(input("Ingresa Tu Nota: "))

if (nota >= 90):
    
    print("Excelente")
    
elif(nota >= 75):
    
    print("Buena Calificacion")
    
elif(nota == 60):
    
    print("Aprobado")    
    
else:
    
    print("Reprobado")