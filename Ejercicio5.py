from turtle import pen


Name = input("Cual es tu nombre?: ")
Edad = int(input("Cual es tu edad?: "))

if Edad <=4:
    precio_entrada = "gratis"
elif Edad >4 and Edad <= 18:
    precio_entrada = 1.50
elif Edad >= 60:
    precio_entrada = 1
else:
    precio_entrada = 2.00

print(f"El cliente: {Name} tiene: {Edad} años y su entrada de cine cuesta: ${precio_entrada}")

