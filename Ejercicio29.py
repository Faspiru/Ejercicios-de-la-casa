palabra = input("Dime una palabra: ").lower()

while palabra.isnumeric():
    palabra = input("Ingreso Invalido, dime una palabra: ")

palabra_nueva = ""

for x in palabra:
    if x in ["a", "e", "i", "o", "u"]:
        palabra_nueva += x.upper()
    else:
        palabra_nueva += x

print(palabra_nueva)