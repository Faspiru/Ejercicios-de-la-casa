info = {
    "shirt_sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    "colors": {
        "plain": "white,black,blue,gray",
        "tie-dye": "rainbow,acid wash"
    },
    "print_sizes": [[(10, 10), 12.30], [(20, 15), 14.60]]
}

# en "print_sizes", la tupla almacena las dimensiones del estampado en centímetros. El número decimal es el precio en dólares

iniciacion_programa = True
contador_compradores = 0
compradores = {}

while iniciacion_programa == True:
    seleccion_inicial = input(" ********************** \n *Menu inicial compras* \n ********************** \n 1. Registrar compra \n 2. Ver compras registradas \n 3. Cerrar programa \n Que desea realizar? \n --> ")
    while not seleccion_inicial.isnumeric() or int(seleccion_inicial) not in range(1, 4):
        seleccion_inicial = input(" ********************** \n *Menu inicial compras* \n ********************** \n 1. Registrar compra \n 2. Ver compras registradas \n 3. Cerrar programa \n Ingreso Invalido. Que desea realizar? \n --> ")
    seleccion_inicial = int(seleccion_inicial)
    
    if seleccion_inicial == 1:
        categories = {1: "plain", 2: "tie-dye"}
        plain_colors = {1: "white", 2: "black", 3: "blue", 4: "gray"}
        tie_dye_colors = {1: "rainbow", 2:"acid wash"}
        print_sizes = {1: (10, 10), 2: (20, 15)}
        costo_franela = {1: 12.30, 2: 14.60}
        cedula = input("Ingrese su cedula: ")
        while not cedula.isnumeric():
            cedula = input("Ingreso Invalido. Ingrese su cedula: ")
        talla_franela = input("\n 0. XXS \n 1. XS \n 2. S \n 3. M \n 4. L \n 5. XL \n 6. XXL\n Que talla desea la franela? \n --> ")
        while not talla_franela.isnumeric() or not int(talla_franela) in range(0, 7):
            talla_franela = input("\n 0. XXS \n 1. XS \n 2. S \n 3. M \n 4. L \n 5. XL \n 6. XXL \n Ingreso Invalido Que talla desea la franela? \n --> ")
        talla_franela = int(talla_franela)
        categoria_color_franela = input("\n 1. plain \n 2. tie-dye \n En que color desea la franela? \n --> ")
        while not categoria_color_franela.isnumeric() or not int(categoria_color_franela) in range(1, 3):
            categoria_color_franela = input("\n 1. plain \n 2. tie-dye \n Ingreso Invalido. En que color desea la franela? \n --> ")
        categoria_color_franela = int(categoria_color_franela)
        if categoria_color_franela == 1:
            plain_color_franela = input(" 0. White \n 1. Black \n 2. Blue \n 3. Gray \n Que color desea? \n --> ")
            while not plain_color_franela.isnumeric() or not int(plain_color_franela) in range(0, 4):
                plain_color_franela = input(" 0. White \n 1. Black \n 2. Blue \n 3. Gray \n Ingreso Invalido. Que color desea? \n --> ")
            plain_color_franela = int(plain_color_franela)
        elif categoria_color_franela == 2:
            tie_dye_color_franela = input(" 0. Rainbow \n 1. Acid Wash \n Que color desea? \n --> ")
            while not tie_dye_color_franela.isnumeric() or not int(tie_dye_color_franela) in range(0, 2):
                tie_dye_color_franela = input(" 0. Rainbow \n 1. Acid Wash \n Ingreso Invalido. Que color desea? \n --> ")
            tie_dye_color_franela = int(tie_dye_color_franela)
        estampado_size = input(" 1. (10, 10) \n 2. (20, 15) \n Que size desea? \n --> ")
        while not estampado_size.isnumeric() or not int(estampado_size) in range(1, 3):
            estampado_size = input(" 1. (10, 10) \n 2. (20, 15) \n Ingreso Invalido. Que size desea? \n --> ")
        estampado_size = int(estampado_size)

        cadena_string = info.get("colors").get(categories.get(categoria_color_franela))
        list_cadena_string = cadena_string.split(",")
        if len(list_cadena_string) == 4:
            color_final_choice = list_cadena_string[plain_color_franela]
        else: 
            color_final_choice = list_cadena_string[tie_dye_color_franela]
        
        cedula_al_reves = cedula[::-1]

        factura = {
            "cedula": cedula,
            "talla franela": info.get("shirt_sizes")[talla_franela],
            "color franela": color_final_choice,
            "estampado size": print_sizes.get(estampado_size),
            "coste franela": f"{costo_franela.get(estampado_size)}$"
        }
        print(" *********** \n **Factura** \n ***********")
        for key, value in factura.items():
            if cedula_al_reves == cedula:
                if key != "coste franela":
                    print(f" {key}: {value}")
                else:
                    print(f" {key}: {value} -> OBTIENE UN DESCUENTO")
            else:
                print(f" {key}: {value}")

        contador_compradores +=1
        compradores[contador_compradores] = factura

    
    elif seleccion_inicial == 2:
        for key, value in compradores.items():
            print(f"Compra {key} --> \n")
            for key_2, value_2 in value.items():
                if cedula_al_reves == cedula:
                    if key_2 != "coste franela":
                        print(f" {key_2}: {value_2}")
                    else:
                        print(f" {key_2}: {value_2} -> OBTIENE UN DESCUENTO")
                else:
                    print(f" {key_2}: {value_2}")
                #print(f"{key_2}: {value_2}")
        
    elif seleccion_inicial  == 3:
        iniciacion_programa = False

