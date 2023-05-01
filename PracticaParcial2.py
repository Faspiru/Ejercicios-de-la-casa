def serie_fibonacci():
    Serie_Fibonacci_List = [0, 1]
    x = 0
    y = 1
    z = 0
    while z < 10000000:
        z = (x) + (y)
        Serie_Fibonacci_List.append(z)
        x = y
        y = z

    return Serie_Fibonacci_List

def main():
    while True:
        numero = input("Ingrese un numero entero positivo: ")
        while not numero.isnumeric() or not int(numero) >0:
            numero = input("Ingreso Invalido. Ingrese un numero entero positivo: ")
        numero = int(numero)

        Serie_Fibonacci_List = serie_fibonacci()
        if numero in Serie_Fibonacci_List:
            print()
            print("El numero esta en la serie de fibonacci")
            print()
        else:
            print()
            print("El numero no esta en la sucesion de fibonacci")
            print()

        keep_proving = input("Desea probar con otro numero? \n 1. Yes \n 2. No \n --> ")
        while not keep_proving.isnumeric() or not int(keep_proving) in range(1, 3):
            keep_proving = input("Ingreso Invalido. Desea probar con otro numero? \n 1. Yes \n 2. No \n --> ")
        
        if keep_proving == "2":
            break
        
main()
