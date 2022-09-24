numero_limite = input("Ingrese el tope de la sucesion de Fibonacci: ")

while not numero_limite.isnumeric() or int(numero_limite) == 0:
    numero_limite = input("Ingreso invalido. Intente de nuevo: ")

x = 0 #f(n - 2)
y = 1 #f(n - 1)
z = 1 #f(n)

sucesion = [str(x), str(y)]

while z <= int(numero_limite):
    sucesion.append(str(z))
    x = y
    y = z
    z = x + y

print(", ".join(sucesion))