#Ejercicio 2
#Fabrizio Spiotta
#Carnet: 20221110261
#Cedula: 30057185

music = {
    "Iron Maiden":{
        "The Number of the Beast": [
            {
                "name": "Run to the Hills",
                "duration": "3:53"
            },
            {
                "name": "Hallowed Be Thy Name",
                "duration": "7:11"
            }
        ],
        "Piece of Mind":[
            {
                "name": "Flight of Icarus",
                "duration": "3:50"
            },
            {
                "name": "The Trooper",
                "duration": "4:12"
            },
            {
                "name": "Quest for Fire",
                "duration": "3:42"
            }
        ],
        "Dance of Death":[
            {
                "name": "No More Lies",
                "duration": "7:21"
            },
            {
                "name": "Dance of Death",
                "duration": "8:36"
            }
        ]
    },
    "Guns N' Roses":{
        "Use Your Illusion I":[
            {
                "name": "Live and Let Die",
                "duration": "3:02"
            },
            {
                "name": "Don't Cry",
                "duration": "4:43"
            },
            {
                "name": "November Rain",
                "duration": "8:56"
            }
        ],
        "Appetite for Destruction":[
            {
                "name": "Welcome to the Jungle",
                "duration": "4:32"
            },
            {
                "name": "Paradise City",
                "duration": "6:45"
            },
            {
                "name": "Sweet Child o' Mine",
                "duration": "5:54"
            }
        ]
    },
    "AC/DC": {
        "Back in Black": [
            {
                "name": "Hells Bells",
                "duration": "5:12"
            },
            {
                "name": "Back in Black",
                "duration": "4:15"
            }
        ]
    }
}

canciones_totales = []
cont_canciones_cola = 0
canciones_validacion = []

iniciacion_programa = True
while iniciacion_programa == True:
    seleccion_inicial = input(" ******************* \n **Album de musica** \n ******************* \n 1. Seleccionar cancion \n 2. Ver cola de reproduccion \n 3. Salir \n Que operacion desea realizar?: ")
    while not seleccion_inicial.isnumeric() or not int(seleccion_inicial) in range (1,4):
        seleccion_inicial = input(" ************************ \n **Album de musica** \n ************************ \n 1. Seleccionar cancion \n 2. Ver cola de reproduccion \n 3. Salir \n Ingreso Invalido. Que operacion desea realizar?: ")
    seleccion_inicial = int(seleccion_inicial)

    if seleccion_inicial == 1:
        dict_bandas = {1: "Iron Maiden", 2: "Guns N' Roses", 3: "AC/DC"}
        dict_albumes = {1: "The Number of the Beast", 2: "Piece of Mind", 3: "Dance of Death", 4: "Use Your Illusion I", 5: "Appetite for Destruction", 6:"Back in Black"}
        banda_seleccion = input(" 1. Iron Maiden \n 2. Guns N' Roses \n 3. AC/DC \n Cual banda desea escuchar? \n --> ")
        while not banda_seleccion.isnumeric() or not int(banda_seleccion) in range(1, 4):
            banda_seleccion = input(" 1. Iron Maiden \n 2. Guns N' Roses \n 3. AC/DC \n Ingreso Invalido. Cual banda desea escuchar? \n --> ") 
        banda_seleccion = int(banda_seleccion)
        if banda_seleccion == 1:
            album_seleccion = int(input(" 1. The Number of the Beast \n 2. Piece of Mind \n 3. Dance of Death \n Cual album desea escuchar? \n --> "))
        elif banda_seleccion == 2:
            album_seleccion = int(input(" 4. Use Your Illusion I \n 5. Appetite for Destruction \n Cual album desea escuchar? \n --> "))
        elif banda_seleccion == 3: 
            album_seleccion = int(input(" 6. Back in Black \n Cual album desea escuchar? \n --> "))
        for banda, album in music.items():
            if banda == dict_bandas.get(banda_seleccion):
                #print(banda)
                for album, canciones_list in album.items():
                    if album == dict_albumes.get(album_seleccion):
                        for cancion in canciones_list:
                            name = cancion.get("name")
                            duration = cancion.get("duration")
                            print(f" name: {name}, duration: {duration}")
                            canciones_validacion.append(name)
                
                        cancion_seleccion = input("Cual es la cancion que desea escuchar? (Escribalo correctamente como aparece por pantalla): ")
                        while cancion_seleccion.isnumeric() or cancion_seleccion not in canciones_validacion:
                            cancion_seleccion = input("Ingreso Invalido. Cual es el id de la cancion que desea escuchar?: ")
                        for cancion in canciones_list:
                            if cancion.get("name") == cancion_seleccion:
                                durationReal =  cancion.get("duration")
                        cancion_escogida_por_usuario = {
                        "banda": banda,
                        "Album": album,
                        "cancion": cancion_seleccion,
                        "duracion": durationReal
                        }
        canciones_totales.append(cancion_escogida_por_usuario)
        cont_canciones_cola += 1

    elif seleccion_inicial == 2:
        if canciones_totales == []:
            print("No hay canciones en cola")
        else:
            for diccionario in canciones_totales:
                print(f"\n")
                for key, value in diccionario.items():
                    print(f"{key}: {value}")
            print(f"\nCanciones totales en cola: {cont_canciones_cola}")
    
    elif seleccion_inicial == 3:
        iniciacion_programa = False