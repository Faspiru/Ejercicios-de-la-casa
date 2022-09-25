numero = input("Ingrese un numero entero positivo: ")

while not numero.isnumeric() or int(numero) == 0:
    numero = input("Ingreso Invalido. Porfavor, Ingrese un numero entero positivo: ")

cont1 = 0 
cont2 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0

numero = str(numero)
numero_voletado = str(numero[::-1])
numero_voletado = int(numero_voletado)
numero = int(numero)
raiz_numero = numero**0.5
raiz_numero = round(raiz_numero, 1)


auxP = 1
divisores = []

for x in range(2, numero):   
    if numero%x == 0:
        cont1 += 1
        divisores.append(x)
    if (x*(x+1)) == numero:
        cont2 += 1
for y in divisores:
    auxP += y 
    if auxP == numero:
        cont4 += 1
    if auxP > numero:
        cont5 +=1
    if auxP < numero:
        cont6 += 1 
    if y**2 in divisores:
        cont7 += 1
if cont1 == 0:
    print("El numero es primo")
if cont1 != 0:
    print(f"El numero es compuesto, y sus divisores son: {divisores}")
if cont2 != 0:
    print("El numero es oblogno")
if numero_voletado == numero:
    print("El numero es palindromo")
if cont4 != 0:
    print("El numero es perfecto")
if cont5 != 0:
    print("El numero es abundante")
if cont6 != 0:
    print("El numero es deficiente")
if (raiz_numero ** 2) == numero:
    print("El numero es cuadrado")
if cont7 == 0:
    print("El numero es libre de cuadrados")
