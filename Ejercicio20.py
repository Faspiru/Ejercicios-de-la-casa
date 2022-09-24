palabra = input("Dime algo: ")

palabra_volteada = palabra[::-1] # inicio en el inicio, llego al final, y empiezo desde el final al inicio. SOLO PARA STRINGS

print(palabra)
print(palabra_volteada)

if palabra == palabra_volteada:
    print('Es un palindromo')
else:
    print("No es palindromo")