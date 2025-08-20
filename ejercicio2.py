import os

os.system


numero1 = int(input("Ingrese el primer Numero: "))
numero2 = int(input("Ingrese el segundo Numero: "))

iguala= numero1 == numero2

print ("Los numeros son iguales: ", iguala)

diferente = numero2 != numero1

print("Los numeros son diferentes: ", diferente)

mayorque = numero1 > numero2

print(numero1, "Es mayor a " ,numero2, ": ", mayorque )

menorque = numero2 < numero1

print(numero2, "Es menor a ", numero1, ": ", menorque)

mayorigual = numero1 >= numero2

print(numero1, "Es mayor o igual a ",numero2, ": ", mayorigual)

menorigual = numero2 <= numero1

print(numero2, "Es menor o igual a ",numero1, ": ", menorigual)

u = numero2 > numero1 and numero1 < numero2

print(numero2, "Es mayor que ",numero1, "Y ",numero1, "Es menor que ",numero2, ": ")

o = numero2 > numero1 or numero1 > numero2

print(numero2, "Es mayor que ",numero1, "O ", numero1, "es mayor que",numero2, ": ", u)

