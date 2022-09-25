numero = input("Ingrese un numero entero positivo: ")

while not numero.isnumeric() or int(numero) == 0:
    numero = input("Ingreso Invalido. Porfavor, Ingrese un numero entero positivo: ")

cont = 0 
divisores = []

numero = int(numero)
for x in range(2, numero):   
    if numero%x == 0:
        cont +=1
        divisores.append(x)

if cont == 0:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo, y tiene {cont} divisores, los cuales son {divisores}")