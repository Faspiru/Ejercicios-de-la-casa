numero = input("Ingrese un numero natural: ")

while not numero.isnumeric() or int(numero) == 0:
    numero = input("Ingreso Invalido, Ingrese un numero natural: ")

while  len(numero) >1:
    aux = 0
    print("aux inicial: ", aux)
    for d in numero:
        aux += int(d)
    numero = str(aux)
    print(aux)