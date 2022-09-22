number = input("Dime un numero: ")
contador = 0

if number.isnumeric():
    number = int(number)
    aux = number - 1
    if number <=1:
        print("The number is not prime")
    else:
        while aux >1:
            if number%aux == 0:
                contador += 1
            aux -= 1
        if contador == 0:
            print("The number is prime")
        else:
            print("The number is not prime")
else:
    print("Invalid Numbers")