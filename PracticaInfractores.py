infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678}, 
}

db={}


Iniciacion_Programa = True
contador_infractores = 0

while Iniciacion_Programa == True:
    seleccion_inicial = input(" ************************ \n **Base De Datos Multas** \n ************************ \n 1. Ingresar un infractor \n 2. Eliminar un infractor \n 3. Mostrar multas registradas \n 4. Filtro de busqueda segun officer \n 5. Cerrar el programa \n Que operacion desea realizar?: ")
    while not seleccion_inicial.isnumeric() or not int(seleccion_inicial) in range (1,6):
        seleccion_inicial = input(" 1. Ingresar un infractor \n 2. Eliminar un infractor \n 3. Mostrar multas registradas \n 4. Filtro de busqueda segun officer \n 5. Cerrar el programa \n Ingreso Invalido, que operacion desea realizar?: ")
    seleccion_inicial = int(seleccion_inicial)

    if seleccion_inicial == 1:
        nuevo_infractor = {}
        nombre_value = input("Cual es su nombre?: ")
        while not nombre_value.isalpha():
            nombre_value = input("Ingreso Invalido. Porfavor, ingrese un nombre valido: ")
        apellido_value = input("Cual es su apellido?: ")
        while not apellido_value.isalpha():
            apellido_value = input("Ingreso Invalido. Porfavor, ingrese un apellido valido: ")
        cedula_value = input("Cual es su cedula?: ")
        while not cedula_value.isnumeric() or not len(cedula_value) == 8:
            cedula_value = input("Ingreso Invalido. Porfavor, ingrese una cedula valida: ")
        tipo_de_infraccion_value = input(" 1. Choque \n 2. Semáforo \n 3. Falta de documentos \n Cual es su infraccion: ")
        while not tipo_de_infraccion_value.isnumeric() or not int(tipo_de_infraccion_value) in range(1,4):
            tipo_de_infraccion_value= input(" 1. Choque \n 2. Semáforo \n 3. Falta de documentos \n Ingreso Invalido. Porfavor, ingrese una opcion valida: ")
        tipo_de_infraccion_value = int(tipo_de_infraccion_value)
        fiscal_value = input(" 1. Luis Bello \n 2. Jose Quevedo \n 3. Antonio Guerra \n Cual es el oficial que le coloco la multa?: ")
        while not fiscal_value.isnumeric() or not int(fiscal_value) in range (1,4):
            fiscal_value = input(" 1. Luis Bello \n 2. Jose Quevedo \n 3. Antonio Guerra \n Ingreso Invalido, cual es el oficial que le coloco la multa?: ")
        tipo_de_infraccion_value = int(tipo_de_infraccion_value)
        fiscal_value = int(fiscal_value)
        nuevo_infractor["nombre"] = nombre_value
        nuevo_infractor["Lname"] = apellido_value
        nuevo_infractor["cedula"] = cedula_value
        nuevo_infractor["infrctn"] = tipo_de_infraccion_value
        nuevo_infractor["fiscal"] = fiscal_value
        decision_if_1 = input(" 1. Agregar infractor a base de datos \n 2. Borrar infractor \n Que desea realizar ahora?: ")
        while not decision_if_1.isnumeric() or not int(decision_if_1) in range (1,3):
            print(" 1. Agregar infractor a base de datos \n 2. Borrar infractor \n Ingreso Invalido, Que desea realizar ahora?: ")
        decision_if_1 = int(decision_if_1)
        if decision_if_1 == 1:
            contador_infractores += 1
            db[contador_infractores] = nuevo_infractor

    
    elif seleccion_inicial == 2:
        for key, value in db.items():
            print(f"{key} --> ")
            for keys_in_values, values_in_values in value.items():
                if keys_in_values == "infrctn":
                    print(f"\t {keys_in_values}: \t {infraction.get(values_in_values).get('name')} {infraction.get(values_in_values).get('cost')}$")
                elif keys_in_values == "fiscal":
                    print(f"\t {keys_in_values}: \t {officers.get(values_in_values).get('name')} {officers.get(values_in_values).get('lastName')} {officers.get(values_in_values).get('ci')}")   
                else:
                    print(f"\t {keys_in_values}: \t {values_in_values}")
        eliminacion = input("Cual infractor desea eliminar? \n --> ")
        while not eliminacion.isnumeric() or int(eliminacion) not in range (1, contador_infractores+1):
            eliminacion = input("Ingreso Invalido. Cual infractor desea eliminar? \n --> ")
        eliminacion = int(eliminacion)
        del db[eliminacion]
    
    elif seleccion_inicial == 3:
        for key, value in db.items():
            print(f"{key} --> ")
            for keys_in_values, values_in_values in value.items():
                if keys_in_values == "infrctn":
                    print(f"\t {keys_in_values}: \t {infraction.get(values_in_values).get('name')} {infraction.get(values_in_values).get('cost')}$")
                elif keys_in_values == "fiscal":
                    print(f"\t {keys_in_values}: \t {officers.get(values_in_values).get('name')} {officers.get(values_in_values).get('lastName')} {officers.get(values_in_values).get('ci')}")   
                else:
                    print(f"\t {keys_in_values}: \t {values_in_values}")
    
    elif seleccion_inicial == 4:
        multas_in_db = []
        filtro_officer = input(" 1. Luis Bello \n 2. Jose Quevedo \n 3. Antonio Guerra \n Desea filtrar los datos de las multas realizadas por cual oficial?: ")
        while not filtro_officer.isnumeric() or not int(filtro_officer) in range(1,4):
            filtro_officer = input(" 1. Luis Bello \n 2. Jose Quevedo \n 3. Antonio Guerra \n Ingreso Invalido. Desea filtrar los datos de las multas realizadas por cual oficial?: ")
        filtro_officer = int(filtro_officer)
        for keydb, valuedb in db.items():
            if valuedb.get("fiscal") == filtro_officer:
                multas_in_db.append(valuedb)
        if multas_in_db == []:
            print("No hay multas registradas con ese oficial")
        else:
            for multa in multas_in_db:
                print(f"{keydb} --> ")
                for key, value in multa.items():
                    if key == "infrctn":
                        print(f"\t {key}: \t {infraction.get(value).get('name')} {infraction.get(value).get('cost')}$")
                    elif key == "fiscal":
                        print(f"\t {key}: \t {officers.get(value).get('name')} {officers.get(value).get('lastName')} {officers.get(value).get('ci')}")   
                    else:
                        print(f"\t {key}: \t {value}")
                    
    elif seleccion_inicial == 5:
        Iniciacion_Programa = False