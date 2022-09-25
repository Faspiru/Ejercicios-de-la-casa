Iniciacion_programa = True

while Iniciacion_programa == True:

    print(" Calculadora basica papito \n 1. Adicion \n 2. Sustraccion \n 3. Multiplicacion \n 4. Division \n 5. Potenciacion")
    operacion = input("Que operacion desea realizar? \n --> ")

    while not operacion.isnumeric() or int(operacion) not in range(1, 6):
        print(" 1. Adicion \n 2. Sustraccion \n 3. Multiplicacion \n 4. Division \n 5. Potenciacion")
        operacion = input("Opcion Invalida, porfavor ingrese una opcion valida: ")

    operacion = int(operacion)

    if operacion == 1:
        n1 = input("Ingrese el primer elemento: ")
        while not n1.isnumeric():
            n1 = input("Ingreso Invalido, porfavor ingrese el primer elemento (numero entero positivo): ")
        n2 = input("Ingrese el segundo elemento: ")
        while not n2.isnumeric():
            n2 = input("Ingreso Invalido, porfavor ingrese el segundo elemento (numero entero positivo): ")
        n1 = int(n1)
        n2 = int(n2)
        resultado_adicion = n1 + n2 
        print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
        decision_adicion = input("Escoga una opcion \n --> ")
        while not decision_adicion.isnumeric() or int(decision_adicion) not in range (1,3):
            print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
            decision_adicion = input("Ingreso invalido, porfavor escoga una opcion valida \n --> ")
        decision_adicion = int(decision_adicion)  
        if decision_adicion == 1:
            print(f"El resultado de la operacion es {resultado_adicion}")
            Iniciacion_programa = False
        elif decision_adicion == 2:
            Iniciacion_programa = True
    elif operacion == 2:
        n1 = input("Ingrese el primer elemento: ")
        while not n1.isnumeric():
            n1 = input("Ingreso Invalido, porfavor ingrese el primer elemento (numero entero positivo): ")
        n2 = input("Ingrese el segundo elemento: ")
        while not n2.isnumeric():
            n2 = input("Ingreso Invalido, porfavor ingrese el segundo elemento (numero entero positivo): ")
        n1 = int(n1)
        n2 = int(n2)
        resultado_sustraccion = n1 - n2 
        print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
        decision_sustraccion = input("Escoga una opcion \n --> ")
        while not decision_sustraccion.isnumeric() or int(decision_sustraccion) not in range (1,3):
            print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
            decision_sustraccion = input("Ingreso invalido, porfavor escoga una opcion valida \n --> ")
        decision_sustraccion = int(decision_sustraccion)
        if decision_sustraccion == 1:
            print(f"El resultado de la operacion es {resultado_sustraccion}")
            Iniciacion_programa = False
        elif decision_sustraccion == 2:
            Iniciacion_programa = True
    elif operacion == 3:
        n1 = input("Ingrese el primer factor: ")
        while not n1.isnumeric():
            n1 = input("Ingreso Invalido, porfavor ingrese el primer factor (numero entero positivo): ")
        n2 = input("Ingrese el segundo factor: ")
        while not n2.isnumeric():
            n2 = input("Ingreso Invalido, porfavor ingrese el segundo factor (numero entero positivo): ")
        n1 = int(n1)
        n2 = int(n2)
        resultado_multiplicacion = n1 * n2 
        print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
        decision_multiplicacion = input("Escoga una opcion \n --> ")
        while not decision_multiplicacion.isnumeric() or int(decision_multiplicacion) not in range (1,3):
            print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
            decision_multiplicacion = input("Ingreso invalido, porfavor escoga una opcion valida \n --> ")
        decision_multiplicacion = int(decision_multiplicacion)
        if decision_multiplicacion == 1:
            print(f"El resultado de la operacion es {resultado_multiplicacion}")
            Iniciacion_programa = False
        elif decision_multiplicacion == 2:
            Iniciacion_programa = True
    elif operacion == 4:
        n1 = input("Ingrese el primer factor: ")
        while not n1.isnumeric():
            n1 = input("Ingreso Invalido, porfavor ingrese el primer factor (numero entero positivo): ")
        n2 = input("Ingrese el segundo factor: ")
        while not n2.isnumeric() or not int(n2) != 0:
            n2 = input("Ingreso Invalido, porfavor ingrese el segundo factor. Ademas tenga cuidado que el segundo factor no sea cero (numero entero positivo): ")
        n1 = int(n1)
        n2 = int(n2)
        resultado_division = n1 / n2 
        print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
        decision_division = input("Escoga una opcion \n --> ")
        while not decision_division.isnumeric() or int(decision_division) not in range (1,3):
            print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
            decision_division = input("Ingreso invalido, porfavor escoga una opcion valida \n --> ")
        decision_division = int(decision_division)
        if decision_division == 1:
            print(f"El resultado de la operacion es {resultado_division}")
            Iniciacion_programa = False
        elif decision_division == 2:
            Iniciacion_programa = True
    elif operacion == 5:
        n1 = input("Ingrese la base ")
        while not n1.isnumeric():
            n1 = input("Ingreso Invalido, porfavor ingrese el primer factor (numero entero positivo): ")
        n2 = input("Ingrese el exponente: ")
        while not n2.isnumeric() or int(n2) == 0:
            n2 = input("Ingreso Invalido, porfavor ingrese el segundo factor y tenga cuidado que el denominador no sea cero, debido a que en matematicas la division por cero no esta definida (numero entero positivo): ")
        n1 = int(n1)
        n2 = int(n2)
        resultado_potenciacion = n1 ** n2 
        print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
        decision_potenciacion = input("Escoga una opcion \n --> ")
        while not decision_potenciacion.isnumeric() or int(decision_potenciacion) not in range (1,3):
            print("Que desea realizar? \n 1. Mostrar resultado \n 2. Eliminar resultado y realizar otra operacion")
            decision_potenciacion = input("Ingreso invalido, porfavor escoga una opcion valida \n --> ")
        decision_potenciacion = int(decision_potenciacion)
        if decision_potenciacion == 1:
            print(f"El resultado de la operacion es {resultado_potenciacion}")
            Iniciacion_programa = False
        elif decision_potenciacion == 2:
            Iniciacion_programa = True