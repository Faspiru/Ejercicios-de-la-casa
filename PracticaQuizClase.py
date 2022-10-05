products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    }
}

iniciacion_Programa = True
objetos_comprados = []

while iniciacion_Programa == True:
    option = int(input("Please enter a valid option \n 1. Show inventory \n 2. Make a purchase \n 3. Print factura \n 4. Exit \n --> "))
    if option == 1:
        categories = {1:"mobiles", 2:"laptops"}
        category = int(input("Please enter a valid category \n 1. mobiles \n 2. laptops \n --> "))
        for type, brands in products.items():
            if type == categories.get(category):
                for brand, list_of_product in brands.items():
                    print(brand)
                    for product in list_of_product:
                        id = product.get("id")
                        name = product.get("name")
                        price = product.get("price")
                        print(f"{id} {name} {price}")

    elif option  == 2:
        product_id = int(input("Please enter the product id you want purchase: "))
        product_selection = None
        for type, brands in products.items():
            for brand, list_of_product in brands.items():
                for product in list_of_product:
                    if product.get("id") == product_id:
                        product_selection = product
                        objetos_comprados.append(product_selection)
                    
        if product_selection:
            print("Su articulo fue comprado correctamente")
        else:
            print("Product selected not found")
    
    elif option == 3:
        total_price = 0
        if objetos_comprados == []:
            print("No se ha realizado ninguna compra")
        else:
            client = {
                    "name": input("Please enter your name: "),
                    "id card": input("Please enter your id card: "),
                    "product id": objetos_comprados,
                }
            print("**********Factura*********")
            for key, value in client.items():
                if key != "product id":
                    print(key, value)
                else:
                    for dic_objeto in objetos_comprados:
                        total_price += dic_objeto.get("price")
                        for key, value in dic_objeto.items():
                            print(key, value)
            print(f"Total price: {total_price}")

    elif option == 4:
        iniciacion_Programa = False
