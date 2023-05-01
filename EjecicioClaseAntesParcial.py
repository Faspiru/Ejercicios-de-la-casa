def get_client_data():
    rif = input("Ingrese su rif: ")
    while not rif.isnumeric():
        rif = input("Ingreso Invalido. Ingrese su rif: ")

    codigo_linea_de_producto = input("Ingrese el codigo de la linea se producto que desea \n Q. Quimico \n F. Farmaceutico \n B. Biologico \n --> ").upper()
    while not codigo_linea_de_producto.isalpha() or not codigo_linea_de_producto == "Q" and not codigo_linea_de_producto == "F" and not codigo_linea_de_producto == "B":
        codigo_linea_de_producto = input("Ingreso Invalido. Ingrese el codigo de la linea se producto que desea \n Q. Quimico \n F. Farmaceutico \n B. Biologico \n --> ").upper()
    
    codigo_forma_de_pago = input("Ingrese su forma de pago \n C. Contado \n R. Credito \n --> ").upper()
    while not codigo_forma_de_pago.isalpha() or not codigo_forma_de_pago == "C" and not codigo_forma_de_pago == "R":
        codigo_forma_de_pago = input("Ingreso Invalido. Ingrese su forma de pago \n C. Contado \n R. Credito \n --> ").upper()
    
    cliente = {
        "rif": rif,
        "Codigo del Producto": codigo_linea_de_producto,
        "Forma de Pago": codigo_forma_de_pago
    }
    return cliente

def get_tax(cliente,products_dict):
    tax = 0
    if cliente.get("Codigo del Producto") == "Q":
        tax += products_dict.get("Q").get("price") * 0.12
    if cliente.get("Codigo del Producto") == "B":
        tax += products_dict.get("B").get("price") * 0.12
    if cliente.get("Forma de Pago") == "R":
        tax += products_dict.get(cliente.get("Codigo del Producto")).get("price") * 0.10
    return tax

def is_prime(cliente):
    prime_bool = False
    ultimo_numero_rif = cliente.get("rif")[-1]
    ultimo_numero_rif = int(ultimo_numero_rif)
    cont_prime = 0
    if ultimo_numero_rif == 0 or ultimo_numero_rif == 1:
        prime_bool = False
    if prime_bool == False:
        for x in range(2, ultimo_numero_rif):
            if ultimo_numero_rif%x == 0:
                cont_prime += 1
    if cont_prime != 0:
        prime_bool = False
    else:
        prime_bool = True
    return prime_bool
    
def get_discount(cliente, products_dict, prime_bool):
    discount = 0
    if cliente.get("Forma de Pago") == "C":
        discount += products_dict.get(cliente.get("Codigo del Producto")).get("price") * 0.03
    if products_dict.get(cliente.get("Codigo del Producto")).get("price")%2 == 0:
        discount += products_dict.get(cliente.get("Codigo del Producto")).get("price") * 0.02
    if prime_bool == True:
        discount += products_dict.get(cliente.get("Codigo del Producto")).get("price") * 0.05
    return discount

def get_total(cliente, discount, tax, products_dict):
    total = products_dict.get(cliente.get("Codigo del Producto")).get("price") + tax - discount
    return total 

def get_receipt(cliente, products_dict, payment_methods, total, discount, tax):
    print("------FACTURA------")
    print(f"Rif: {cliente.get('rif')}")
    print(f"Linea de Producto: {products_dict.get(cliente.get('Codigo del Producto')).get('description')}")
    print(f"Tipo de Pago: {payment_methods.get(cliente.get('Forma de Pago'))}")
    print("-------------------")
    print(f"Monto del Descuento: {discount}")
    print(f"Monto del Impuesto: {tax}")
    print(f"Monto Total a Pagar: {total}")

def get_final_day_data(clientes):
    contQ = 0
    contF = 0 
    contB = 0
    discountC = 0
    discountR = 0
    total_facturado_final_day = 0
    total_max = 0
    rifs_maxs = []

    for cliente in clientes:
        total_facturado_final_day += cliente.get("Monto Total a Pagar")
        if cliente.get("Forma de Pago") == "C":
            discountC += cliente.get("Monto del Descuento")
        if cliente.get("Forma de Pago") == "R":
            discountR += cliente.get("Monto del Descuento")
        if cliente.get("Codigo del Producto") == "Q":
            contQ += 1
        if cliente.get("Codigo del Producto") == "B":
            contB += 1
        if cliente.get("Codigo del Producto") == "F":
            contF += 1
        if cliente.get("Monto Total a Pagar") == total_max:
            rif_max = cliente.get("rif")
            rifs_maxs.append(rif_max)
        while cliente.get("Monto Total a Pagar") > total_max:
            rif_max = ""
            total_max = cliente.get("Monto Total a Pagar")
            rif_max = cliente.get("rif")
            rifs_maxs.append(rif_max)
            
    print("------FINAL DAY DATA------")
    print(f"Cantidad de compradores de productos Quimicos: {contQ}")
    print(f"Cantidad de compradores de productos Farmaceutricos: {contF}")
    print(f"Cantidad de compradores de productos biologicos: {contB}")
    print(f"Cantidad de descuentos en compradores que pagaron por contado: {discountC}")
    print(f"Cantidad de descuentos en compradores que pagaron por credito: {discountR}")
    print(f"Rif de comprador para la compra mas alta: ")
    for rif in rifs_maxs:
        print(rif)
    print(f"Montos totales facturados: {total_facturado_final_day}")
    
def main():
    products_dict = {
        "Q": {
            "description": "Quimico",
            "price": 1000
        },
        "F": {
            "description": "Farmaceutico",
            "price": 2500
        },
        "B": {
            "description": "Biologico",
            "price": 4000
        }
    }
    
    payment_methods = {
        "C": "Contado",
        "R": "Credito"
    }

    clientes = []

    while True:
        print("------BIENVENIDO------")
        cliente = get_client_data()
        clientes.append(cliente)
        tax = get_tax(cliente, products_dict)
        prime_bool = is_prime(cliente)
        discount = get_discount(cliente, products_dict, prime_bool)
        total = get_total(cliente, discount, tax, products_dict)
        cliente["Monto del Descuento"] = discount
        cliente["Monto del Impuesto"] = tax
        cliente["Monto Total a Pagar"] = total
        get_receipt(cliente, products_dict, payment_methods, total, discount, tax)

        keep_adding_clients = input("Que desea realizar? \n 1. Agregar Cliente \n 2. Salir \n --> ")
        while not keep_adding_clients.isnumeric() or not int(keep_adding_clients) in range(1, 3):
            keep_adding_clients = input("Ingreso Invalido. Que desea realizar? \n 1. Agregar Cliente \n 2. Salir \n --> ")
        if keep_adding_clients == "2":
            break
    get_final_day_data(clientes)
    
main()