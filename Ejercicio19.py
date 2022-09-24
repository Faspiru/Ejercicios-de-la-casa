lista = [123, 4123, 124, 352, 
64352, 324, 6347, 36352, 827, 123, 3479]

contador = 0
suma = 0

i = 0

while len(lista) >= i+1: #Longitud me da 11 cosas, y el indice 10, por eso le pongo mas uno 
    print(i)
    print(lista[i])
    if lista[i] % 2 != 0:
        print("impar")
        contador += 1
        if contador <= 5:
            suma += lista[i]
        print(contador)
        print(suma)
    i += 1
