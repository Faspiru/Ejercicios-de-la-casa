from re import L


pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}

inicio_programa = True

cont_pacientes = 0
pacientes = {}
while inicio_programa == True:
    seleccion_inicial = input(" ********************* \n ***Menu De Clinica*** \n ********************* \n 1. Registrar Paciente \n 2. Ver Pacientes \n 3. Salir \n Que desea realizar? \n --> ")
    while not seleccion_inicial.isnumeric() or not int(seleccion_inicial) in range(1, 4):
        seleccion_inicial = input(" ********************* \n ***Menu De Clinica*** \n ********************* \n 1. Registrar Paciente \n 2. Ver Pacientes \n 3. Salir \n Ingreso Invalido, que desea realizar \n --> ")
    seleccion_inicial = int(seleccion_inicial)

    if seleccion_inicial == 1:
        cont_pacientes +=1
        patologia_individual = []
        patologia_categorias = {1: "Respiratory system", 2: "Nervous system", 3: "Endocrine system"}
        nombre_paciente = input("Porfavor, introduzca su nombre: ")
        while nombre_paciente.isnumeric():
            nombre_paciente = input("Ingreso Invalido. Porfavor, introduzca su nombre: " )
        apellido_paciente = input("Porfavor, introduzca su apellido: ")
        while apellido_paciente.isnumeric():
            apellido_paciente = input("Ingreso Invalido. Porfavor, introduzca su apellido: " )
        cedula_paciente = input("Porfavor, introduzca su cedula: ")
        while not cedula_paciente.isnumeric():
            cedula_paciente = input("Ingreso Invalido. Porfavor, introduzca su cedula: " )
        patologia_grupo_paciente = input(" 1. Respiratory system \n 2. Nervous system \n 3. Endocrine system \n A que grupo pertenece su patologia? \n --> ")
        while not patologia_grupo_paciente.isnumeric() or not int(patologia_grupo_paciente) in range(1, 4):
            patologia_grupo_paciente = input(" 1. Respiratory system \n 2. Nervous system \n 3. Endocrine system \n Ingreso Invalido. A que grupo pertenece su patologia? \n --> ")
        patologia_grupo_paciente = int(patologia_grupo_paciente)
        id_patologia = input("Cual es el id de la patologia que padece? \n --> ")
        while not id_patologia.isnumeric():
            id_patologia = input("Ingreso Invalido. Cual es el id de la patologia que padece? \n --> ")
        id_patologia = int(id_patologia)
        for grupoPatologico, patologia in pathologies.items():
            for list in patologia:
                if list.get("id") == id_patologia:
                    patologia_individual.append(list)
        
    
        paciente = {
        "nombre": nombre_paciente,
        "apellido": apellido_paciente,
        "cedula": cedula_paciente,
        "grupo de la patologia": patologia_categorias.get(patologia_grupo_paciente),
        "id": patologia_individual
    }
        print(paciente)
        for key, value in paciente.items():
            if key != "id":
                print(key, value)
            else:
                for diccionario in patologia_individual:
                    for keys, values in diccionario.items():
                        print(keys, values)
        pacientes[cont_pacientes] = paciente
        
    
    elif seleccion_inicial == 2:
        #print(pacientes)
        filtro_patologico = []
        filtro_patologia = input("Desea filtrar los pacientes por cual patologia? \n --> (id) ")
        while not filtro_patologia.isnumeric() or not int(filtro_patologia) in range(1, 9):
            filtro_patologia = input("Ingreso Invalido. Desea filtrar los pacientes por cual patologia? \n --> (id) ")
        filtro_patologia = int(filtro_patologia)
        for key, value in pacientes.items():
            #print(f"{key} --> ")
            for keyy, valuee in value.items():
                if keyy == "id":
                    for dict in valuee:
                        for keyyy, valueee in dict.items():
                            if dict.get("id") == filtro_patologia:
                                filtro_patologico.append(value)
                                break
        
        if filtro_patologico == []:
            print("No hay pacientes registrados con esa patologia")
        else:
            for dictionary in filtro_patologico:
                for keyss, valuess in dictionary.items():
                    if keyss != "id":
                        print(keyss, valuess)
                    else:
                        for di in valuess:
                            for keysss, valuesss in di.items():
                                print(keysss, valuesss)    
        
        
        #print(filtro_patologico)
        
    

    elif seleccion_inicial == 3:
        inicio_programa = False