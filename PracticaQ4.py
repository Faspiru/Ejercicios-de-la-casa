numero = input("Please, enter a number: ")
while not numero.isnumeric():
    numero = input("Invalid Input. Please, enter a number: ")
numero = int(numero)

paridad = False
if numero%2 == 0:
    paridad = True

Numero_Triangular = False
aux = 0 
for x in range(1, numero):
    aux += x
    if aux == numero:
        Numero_Triangular = True
        break

if paridad == True and Numero_Triangular == True:
    print("El numero es par y triangular")
if Numero_Triangular == True and paridad == False:
    print("El numero es triangular, pero no par")
if Numero_Triangular == False and paridad == True:
    print("El numero es par, pero no triangular")
if Numero_Triangular == False and paridad == False:
    print("El numero no es par y no es triangular")