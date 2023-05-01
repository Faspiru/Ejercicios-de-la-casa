numero = input("Ingrese un numero: ")
while not numero.isnumeric() or not int(numero) >0:
    numero = input("Ingreso Invalido. Ingrese un numero: ")
numero = int(numero)

def impar_numbers_list(numero):
    impar_numbers = []
    for x in range(1, numero+1):
        if x%2 != 0:
            impar_numbers.append(x)
    return impar_numbers

def prime_numbers_list(lista_de_impares):
    prime_numbers = [1, 2]
    for x in lista_de_impares:
        cont = 0
        for y in range (2, x):
            if x%y == 0:
                cont += 1
        if cont == 0:
            if x not in prime_numbers:
                prime_numbers.append(x)
    return prime_numbers

def output_list_numbers(lista_de_primos, numero):
    output_list = []
    cont = 0
    while cont < len(lista_de_primos):
        numero_fijo = lista_de_primos[cont]
        for x in lista_de_primos:
            if numero_fijo * x == numero:
                output_list.append(numero_fijo)
                #output_list.append(x)
        cont += 1
    return output_list


lista_de_impares = impar_numbers_list(numero)
lista_de_primos = prime_numbers_list(lista_de_impares)
lista_final = output_list_numbers(lista_de_primos, numero)

if lista_final == []:
    print("Error")
else:
    n1 = lista_final[0]
    n2 = lista_final[1]
    print(f"el producto de los numeros {n1} y {n2} da como resultado el numero {numero}")
