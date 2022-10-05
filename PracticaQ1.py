## Ejercicio 1

numero = input("Porfavor, ingrese un numero entero positivo: ")
while not numero.isnumeric() or int(numero) == 0:
    numero = input("Ingreso Invalido. Porfavor,ingrese un numero entero positivo: ")

cont_repunit = 0
primer_numero = str(numero[0])
cont_divisores = 0
divisores = []

numero = int(numero)
raiz_numero = numero**(1/2)
raiz_numero = round(raiz_numero, 1)

for x in str(numero):
    if primer_numero != x:
        cont_repunit += 1

if cont_repunit == 0:
    print(f"El numero {numero} es un numero repunit")
else:
    print(f"El numero {numero} no es un numero repunit")
if raiz_numero ** 2 == numero:
    print(f"El numero {numero} es un numero cuadrado")
else:
    print(f"El numero {numero} no es un numero cuadrado")


## Ejercicio 2


