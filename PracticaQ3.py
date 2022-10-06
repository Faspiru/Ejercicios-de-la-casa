numero = input("Dime un numero: ")
list = list(numero)
x = list[0]
y = list[1]
cont = 0 
cont2 = 0
for i in list:
    if x!=i:
        cont +=1 
for z in list:
    if z!= y and x:
        cont2 += 1
if cont == 0:
    print("El numero es camarada")
if cont2 == 0:
    print("El numero es ondulado")



