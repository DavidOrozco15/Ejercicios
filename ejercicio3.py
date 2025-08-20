import os

os.system

nombre = input("Hola, Ingresa Tu Nombre Por Favor: ")
edad = int(input("Por Favor Ingrese Su Edad: "))
nota1 = float(input("Ingrese Su Primera Nota: "))
nota2 = float(input("Ingrese Su Segunda Nota Nota: "))

promedio = (nota1 + nota2) / 2

print(f"Hola {nombre}, tu edad es {edad} y Tu Promedio es: {promedio}" )