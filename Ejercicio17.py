number = input("Ingrese un numero: ")

if number.isnumeric():
    number = int(number)
    while number >= 10:
        suma = 0
        for x in str(number):
            suma = suma + int(x)
        number = suma
    print(suma)
else:
    print("Invalid Numbers")