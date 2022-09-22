Word = input("Introduza una palabra: ").lower()
Reverse = Word[::-1]

if Word == Reverse:
    print("La palabra o numero introducido es un palindromo")
else:
    print("La palabra o numero introducido no es un palindromo")