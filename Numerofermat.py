numero = input("Dime un numero: ")
while not numero.isnumeric:
    numero = input("Ingreso Invalido. Dime un numero: ")
numero = int(numero)
cont1 = 0 
cont2 = 0 
for n in range(0, numero+1):
    if (2**(2**n))+1 == numero:
        cont1 += 1

for x in range(2,numero):
    if numero%x == 0:
        cont2 += 1

if cont1 != 0 and cont2 == 0:
    print("El numero es primo de fermat")
else:
    print("El numero no es primo de fermat")