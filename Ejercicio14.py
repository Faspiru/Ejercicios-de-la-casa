temperatura = input("Cual es la temperatura?: ")

if temperatura.isnumeric():
    if temperatura > 10:
        print("Hace calor")
    elif temperatura > 0 and temperatura <10:
        print("Clima intermedio")
    else:
        print("Hace frio")
else:
    print("Invalid Numbers")

