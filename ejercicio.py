print("Conversor de temperatura")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = int(input("Elige una opción (1 o 2): "))

if opcion == 1:
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C = {fahrenheit}°F")
else:
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")