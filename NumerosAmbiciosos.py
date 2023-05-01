def suma_divisores_exactos(numero):
    suma_divisores = 1
    divisores = [1]
    for x in range(2, numero):
        if numero%x ==0:
            divisores.append(x)
            suma_divisores += x
    return suma_divisores
    

def numeros_perfectos(suma_divisores, suma_divisores_internos):
    numero_perfecto = False
    if suma_divisores_internos == suma_divisores:
        numero_perfecto = True
    return numero_perfecto

def numero_ambicioso(numeros_perfecto):
    if numeros_perfecto == True:
        print("El numero es ambicioso")
    else:
        print("El numero no es ambicioso")

def main():
    while True:
        print("--------BIENVENIDO--------")
        numero = input("Ingrese un numero enter positivo: ")
        while not numero.isnumeric() or not int(numero)>0:
            numero = input("Ingreso Invalido. Ingrese un numero entero positivo")
        numero = int(numero)
        suma_divisores = suma_divisores_exactos(numero)
        suma_divisores_internos = suma_divisores_exactos(suma_divisores)
        numero_perfecto = numeros_perfectos(suma_divisores, suma_divisores_internos)
        while not numero_perfecto == True and suma_divisores != 1:
            suma_divisores_internos = suma_divisores_exactos(suma_divisores)
            numero_perfecto  = numeros_perfectos(suma_divisores, suma_divisores_internos)
            suma_divisores = suma_divisores_internos
        numero_ambicioso(numero_perfecto)
        keep_going = input(" 1. Salir \n 2. Continuar \n Que desea realizar --> ")
        while not keep_going.isnumeric() or not int(keep_going) in range (1, 3):
            keep_going = input(" 1. Salir \n 2. Continuar \n Ingreso Invalido. Que desea realizar --> ")
        if keep_going == "1":
            break

main()