import os

os.system

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
indice_masa_corporal = peso/(altura**2)

match indice_masa_corporal:
    case _ if indice_masa_corporal < 18.5:
        print(f"Usted tiene bajo peso y su imc es: {indice_masa_corporal:.2f} ")
        
    case _ if indice_masa_corporal >= 18.5 and indice_masa_corporal < 24.9:
        print(f"Usted tiene un peso normal y us imc es: {indice_masa_corporal:.2f}")


    case _ if indice_masa_corporal >= 24.9 and indice_masa_corporal < 29.9:
        print(f"Usted tiene sobrepeso y su imc es; {indice_masa_corporal:.2f}")
        
    case _:
        print(f"Usted tiene obesidad y su imc es: {indice_masa_corporal:.2f}")
            
