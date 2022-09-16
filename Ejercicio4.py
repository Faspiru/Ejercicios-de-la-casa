n1 = int(input("Dime un numero pa: "))

if abs(n1%2) == 0 and n1>0:
    print("El numero", n1, "es par y positivo")
elif abs(n1%2) == 0 and n1<0:
    print("El numero", n1, "es par y negativo")
elif abs(n1%2) == 1 and n1>0:
    print("El numero", n1, "es impar y positivo")
elif abs(n1%2) == 1 and n1<0:
    print("El numero", n1, "es impar y negativo")
else:
    print("Error.")

print("Fin.")
