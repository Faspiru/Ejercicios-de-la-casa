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

contador_infractores = 0
iniciacion_programa = True

while iniciacion_programa == True:
    seleccion_inicial = input(" ************************ \n **Base De Datos Multas** \n ************************ \n 1. Ingresar un infractor \n 2. Eliminar un infractor \n 3. Mostrar multas registradas \n 4. Filtro de busqueda segun officer \n 5. Cerrar el programa \n Que operacion desea realizar?: ")
    while not seleccion_inicial.isnumeric() or not int(seleccion_inicial) in range (1,6):
        seleccion_inicial = input(" 1. Ingresar un infractor \n 2. Eliminar un infractor \n 3. Mostrar multas registradas \n 4. Filtro de busqueda segun officer \n 5. Cerrar el programa \n Ingreso Invalido, que operacion desea realizar?: ")
    seleccion_inicial = int(seleccion_inicial)

    #infractor_string = ""
    #for keys_db, values_db in db.items():
        #values_db = dict(values_db)
        #keys_db = str(keys_db)
        #infractor_string += keys_db + " --> "
        #for keys_in_values_db, values_in_values_db in values_db.items():
            #values_for_print =  ", ".join(values_in_values_db)
            #values_in_values_db = str(values_in_values_db)
            #infractor_string += values_in_values_db + " "
        #infractor_string += "."
        #infractor_string += "\n"

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
        fiscal_value = int(fiscal_value)
        nuevo_infractor["name infctr"] = nombre_value
        nuevo_infractor["lastname"] = apellido_value
        nuevo_infractor["cedula"] = cedula_value
        desglose_de_infraccion = infraction[tipo_de_infraccion_value]
        nuevo_infractor["infraccion"] = desglose_de_infraccion["name"] 
        nuevo_infractor["$ infraccion"] = desglose_de_infraccion["cost"]
        #desglose_de_officer = tipo_de_infraccion_value
        nuevo_infractor["fiscal"] = fiscal_value
        #nuevo_infractor["apellido f"] = desglose_de_officer["lastName"]
        #nuevo_infractor["ci fiscal"] = desglose_de_officer["ci"]
        decision_if_1 = input(" 1. Agregar infractor a base de datos \n 2. Borrar infractor \n Que desea realizar ahora?: ")
        while not decision_if_1.isnumeric() or not int(decision_if_1) in range (1,3):
            print(" 1. Agregar infractor a base de datos \n 2. Borrar infractor \n Ingreso Invalido, Que desea realizar ahora?: ")
        if int(decision_if_1) == 1:
            contador_infractores += 1
            db[contador_infractores] = nuevo_infractor
    
    elif seleccion_inicial == 2:
        if db == {}:
            print("\n La lista de infractores esta vacia \n")
        else:
            for keys, values in db.items():
                print(f" \n {keys} --> ")
                values = dict(values)
                for keys_in_db, values_in_db in values.items():
                    print(f"\t {keys_in_db}: \t {values_in_db}")
            eliminacion_infrcator = input("\n Que infractor desea eliminar? \n --> ")
            while not eliminacion_infrcator.isnumeric() or not int(eliminacion_infrcator) in range(1, contador_infractores+1):
                eliminacion_infrcator = input("\n Ingreso Invalido. Que infractor desea eliminar? \n --> ")
            del db[int(eliminacion_infrcator)]
    
    elif seleccion_inicial == 3:
        if db == {}:
            print("\n La lista de infractores esta vacia \n")
        else:
            for keys, values in db.items():
                print(f" \n {keys} --> ")
                values = dict(values)
                for keys_in_db, values_in_db in values.items():
                    print(f"\t {keys_in_db}: \t {values_in_db}")
            
    elif seleccion_inicial == 4:
        db_multas = []

        filtro_officer = input(" 1. Luis Bello \n 2. Jose Quevedo \n 3. Antonio Guerra \n Desea filtrar los datos de las multas realizadas por cual oficial?: ")
        while not filtro_officer.isnumeric() or not int(filtro_officer) in range(1,4):
            filtro_officer = input(" 1. Luis Bello \n 2. Jose Quevedo \n 3. Antonio Guerra \n Ingreso Invalido. Desea filtrar los datos de las multas realizadas por cual oficial?: ")
        filtro_officer = int(filtro_officer)
        for values in db.values():
            if values.get("fiscal") == filtro_officer:
                db_multas.append(values)
        for multa in db_multas:
            for key, value in multa.items():
                if key == "fiscal":
                    print(key, officers.get(value).get("name"), officers.get(value).get("lastName"), officers.get(value).get("ci"))
                else:
                    print(key, value)
                

        


        #if filtro_officer == 1:
            #for keys, values in db.items():
                #values = dict(values)
                #for keys_in_db, values_in_db in values.items():
                    #if values_in_db == "Luis":
                        #print(f"\t {keys_in_db}: \t {values_in_db}")
                    #else:
                       #print(f"No hay multas puestas por dicho officer")

    elif seleccion_inicial == 5:
        iniciacion_programa = False