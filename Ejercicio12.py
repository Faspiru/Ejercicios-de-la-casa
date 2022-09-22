frase = input("Frase: ").lower()
frase_final = ""

for Index in frase:
    if Index in ("a", "e", "i", "o", "u"):
        Index = Index.upper()
        frase_final += Index
    else:
        frase_final += Index

print(frase_final)
