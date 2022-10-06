numero = input("Dime un numero: ")

list_numero = list(numero)

i1 = 0
i2 = 1
i3 = 2
i4 = 3

if len(list_numero)%2 == 0:
    for x in list_numero:
        first_par = (str(list_numero[i1]) + str(list_numero[i2]))
        secon_par = (str(list_numero[i3]) + str(list_numero[i4]))

if int(first_par)*int(secon_par) == int(numero):
    print("El numero es vampiro")
if int(first_par[::-1])*int(secon_par[::-1]) == int(numero):
    print("El numero es vampiro")
if int(first_par[::-1])*int(secon_par) == int(numero):
    print("El numero es vampiro")
if int(first_par)*int(secon_par[::-1]) == int(numero):
    print("El numero es vampiro")