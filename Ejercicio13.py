number = input("Please, enter a number: ")
resultado = 0
resultado2 = 0

for x in str(number):
    resultado = resultado + int(x)

resultado1 = resultado

if resultado <10:
   print(resultado) 
else:
    while resultado1 >10:
        for y in str(resultado1):
            resultado1 = resultado2 + int(y)
            resultado2 = resultado1
    print(resultado1)

print("Fin.")