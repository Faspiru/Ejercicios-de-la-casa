## Factorial 2



def factorial(n):
    f = 1
    for x in range(2, n+1):
        f = f*x
    return f
    



def main():
    while True:
        try:
            numero = int(input("Ingrese un numero natural: "))
            if numero == 0:
                raise Exception
            break
        except ValueError:
            print("Revisa tu tipo de dato")
        except IndentationError:
            print("Revisa tus margenes")
        except:
            print("Error desconocido")
    
    factorialR = factorial(numero)
    print(f"El factorial del numero {numero} es {factorialR}")
        

main()