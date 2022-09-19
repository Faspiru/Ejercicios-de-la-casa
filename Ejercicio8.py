Name = input("Cual es tu nombre?: ")
Edad = input("Cual es tu edad?: ")
Ingresos = input("Cuales son tus ingresos?: ")

if Edad.isnumeric() and Ingresos.isnumeric:
    Edad = float(Edad)
    Ingresos = float(Ingresos)
    if Edad >= 16 and Ingresos >= 1000:
        print(f"El usuario {Name} tiene que tributar")
    else:
        print(f"El usuario {Name} no tiene que tributar")
else:
    print("Invalid Numbers")