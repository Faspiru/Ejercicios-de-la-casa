tabla_desde = input("Tabla de multiplicar del: ")
while not tabla_desde.isnumeric or not int(tabla_desde) >= 0:
    print("Ingreso Invalido, Tabla de multiplicar desde: ")
tabla_hasta = input("Tabla de multiplicar hasta: ")
while not tabla_hasta.isnumeric or not int(tabla_hasta) >= 0:
    print("Ingreso Invalido, Tabla de multiplicar hasta: ")
desde = input("Desde el: ")
while not desde.isnumeric or not int(desde) >= 0:
    print("Ingreso Invalido, Desde el: ")
hasta = input("Hasta el: ")
while not hasta.isnumeric or not int(hasta) >= 0:
    print("Ingreso Invalido, Hasta el: ")

tabla_desde = int(tabla_desde)
tabla_hasta = int(tabla_hasta)
desde = int(desde)
hasta = int(hasta)

for x in range(tabla_desde, tabla_hasta + 1): 
    print(f"\nTabla del {x}\n ")
    for i in range(desde, hasta + 1):
        print(f"{i} x {x} = {i*x}")