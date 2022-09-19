from unicodedata import name


Name = input("Cual es tu nombre?: ")
Gender = input("Cual es tu sexo (M o H)?: ")

if Gender.upper() == "M":
    if Name.upper() < "M":
        group = "A"
    else:
        group = "B"
elif Gender.upper() == "H":
    if Name.upper() > "N":
        group = "A"    
    else:
        group = "B"
else:
    print("Error")

print(f"El grupo de {Name} es {group}")