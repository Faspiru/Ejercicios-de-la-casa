#Ejercicio Bonus
#Fabrizio Spiotta
#Carnet: 20221110261
#Cedula: 30057185

numero = input("Please enter a number: ")
while not numero.isnumeric() or not int(numero)>0:
    numero = input("Invalid Number. Please enter a valid number: ")

list = list(numero)
if len(list) == 1:
    print("El numero es un numero repunit")
else:
    x = list[0]
    y = list[1]
    cont = 0 
    for i in list:
        if x!=i:
            cont +=1 

    if cont == 0:
        print("El numero es un numero repunit")
    else:
        print("El numero no es un numero repunit")