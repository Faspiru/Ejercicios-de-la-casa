#Ejercicio 1
#Fabrizio Spiotta
#Carnet: 20221110261
#Cedula: 30057185

numero = input("Please enter a number: ")
while not numero.isnumeric() or not int(numero)>0:
    numero = input("Invalid number. Please enter a valid number: ")

list_numero = list(numero)

while not len(list_numero) == 1:
    resultado = 0
    for x in list_numero:
        x = int(x)
        resultado = int(resultado)
        resultado += (x**2)
    resultado = str(resultado)
    list_resultado = list(resultado)
    list_numero = list_resultado

if int(resultado) == 1:
    print("El numero es feliz")
else:
    print("El numero no es feliz")