number = input("Dime un numero: ")
valid = False

if number.isnumeric():
    number = int(number)
    aux = number - 1
    if number <= 1:
        print("The number is not prime")
    else:
        while aux > 1: 
            if number%aux == 0:
                valid = True
            aux -= 1
        if valid == False:
            print("The number is prime")
        else:
            print("The number is not prime")
else:
    print("Invalid Numbers")
            

