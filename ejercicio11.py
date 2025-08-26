import os
import random

x = random.randint(1, 10)
print(x)  

os.system("cls")
print("Bienvenido al Minijuego de adivinar un numero entre 1 y 10")

numero = int(input("Ingrese el numero que cree que es el numero: "))

while numero != x:
    if numero < x:
        print("El número es mayor.")
    elif numero > x:
        print("El número es menor.")
    
    numero = int(input("Ingrese el numero que cree que es el numero: "))

print("Felicidades, adivinaste el número")