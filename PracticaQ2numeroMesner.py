numero = input("Introduzca un numero natural: ")
while not numero.isnumeric() or not int(numero)>0:
    numero = input("Ingreso Invalido. Introduzca un numero natural: ")

numero = int(numero)
cont = 0 
cont_mesrenne = 0


for numerito in range (2, numero):
    if numero%numerito == 0:
        cont += 1

if cont == 0:
    for x in range (1, numero+1):
        if numero == ((2**x)-1):
            cont_mesrenne += 1

if cont_mesrenne != 0:
     print("El numero es primo de mersenne")
else:
    print("El numero no es primo de mersenne")