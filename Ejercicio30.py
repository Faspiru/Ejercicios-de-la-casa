numero = input("Ingrese un nunero entero positivo: ")

while not numero.isnumeric():
    numero = input("Ingreso Invalido. Porfavor ingrese un nunero entero positivo: ")

numero = int(numero)
producto = 1

for i in range(1, numero+1):
    producto = producto * i

print(f"El factorial del numero {numero} es {producto}")