def goal_parser(palabra):
    palabra_cambiada = palabra.replace("()", "o")
    palabra_cambiada = palabra_cambiada.replace("(al)", "al") 
    return palabra_cambiada

def main():
    palabra = input("Ingrese una palabra: ")
    while palabra.isnumeric():
        palabra = input("Ingreso Invalido. Ingrese una palabra: ")
    print(goal_parser(palabra))
main()