sexo = input("Ingrese su sexo, (M o F): ").upper()
while not sexo.isalpha() or not sexo == "M" and not sexo == "F":
    sexo = input("Ingreso Invalido. Ingrese su sexo: ").upper()

print(sexo)