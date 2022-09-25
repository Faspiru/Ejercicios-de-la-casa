numero = input("Ingrese un numero entre el 2 y el 12: ")

while not numero.isnumeric() or int(numero) not in range(2,13):
    numero = input("Ingreso Valido, Ingrese un numero entre el 2 y el 12: ")
numero = int(numero)

combinaciones = []

for x in range(1, 7):
    if sorted([x, (numero-x)]) not in combinaciones and (numero-x) in range(1, 7):
        combinaciones.append([x, (numero-x)])

print(combinaciones)


