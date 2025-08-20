import os

os.system

manzana = 2000
pera = 3000
mango = 5000

opcion = input("Ingrese la fruta para consultar su precio (manzana, pera y mango): ").lower()

match opcion:
    case _ if opcion == "manzana":
        print(f"El valor de la manzana es de ${manzana}.")
    case _ if opcion == "pera":
        print(f"El valor de la manzana es de ${pera}.")
    case _ if opcion == "mango":
        print(f"El valor de la manzana es de ${mango}.")
                
    case _:
        print(f"Ingresa una fruta valida")    