def get_client_data(product_line, payment_method):
    codigo_comprador = input("Introduzca su cedula: ")
    while not codigo_comprador.isnumeric():
        codigo_comprador = input("Ingreso Invalido. Introduzca su cedula: ")
    
    linea_de_producto = input(" Que linea de producto desea comprar? \n 1. Quimicos (Q) \n 2. Farmaceuticos (F) \n --> ").upper()
    while not linea_de_producto.isalpha() or not linea_de_producto == "Q" and not linea_de_producto == "F":
        linea_de_producto = input(" Ingreso Invalido. Que linea de producto desea comprar? \n 1. Quimicos (Q) \n 2. Farmaceuticos (F) \n --> ").upper()

    forma_de_pago = input(" Cual es su metodo de pago? \n 1. Contado (C) \n 2. Credito (R) \n --> ").upper()
    while not forma_de_pago.isalpha() or not forma_de_pago == "C" and not forma_de_pago == "R":
        linea_de_producto = input(" Ingreso Invalido. Cual es su metodo de pago? \n 1. Contado (C) \n 2. Credito (R) \n --> ").upper()
    
    cliente = {
        "Codigo Comprador": codigo_comprador,
        "Linea De Producto": product_line.get(linea_de_producto).get("description"),
        "Forma De Pago": payment_method.get(forma_de_pago),
        "Subtotal a Pagar": product_line.get(linea_de_producto).get("price")
    }
    return cliente

def get_subtotal(cliente):
    subtotal = cliente.get("Subtotal a Pagar")
    return subtotal

def get_IVA(cliente, subtotal):
    IVA = 0
    if cliente.get("Linea De Producto") == "Quimicos":
        IVA += subtotal * 0.12
    return IVA

def get_total_amount(subtotal, IVA):
    monto_total_a_pagar = subtotal + IVA
    return monto_total_a_pagar

def get_final_day_status(clientes):
    contQ = 0
    contF = 0
    IVA_en_Contado = 0
    IVA_en_Credito = 0
    monto_total_facturado = 0
    for cliente in clientes:
        monto_total_facturado += cliente.get("Total a Pagar")
        if cliente.get("Linea De Producto") == "Quimicos":
            contQ += 1
        if cliente.get("Linea De Producto") == "Farmaceuticos":
            contF += 1
        if cliente.get("Forma De Pago") == "Contado":
            IVA_en_Contado += cliente.get("IVA")
        if cliente.get("Forma De Pago") == "Credito":
            IVA_en_Credito += cliente.get("IVA")

    print("----------------------------")
    print("---------FINAL DAY----------")
    print("----------------------------")
    print()
    print(f"Cantidad de compradores para productos quimicos: {contQ}")
    print(f"Cantidad de compradores para productos farmaceuticos: {contF}")
    print(f"impuesto cobrado para los que pagaron en contado: {IVA_en_Contado}")
    print(f"impuesto cobrado para los que pagaron en credito: {IVA_en_Credito}")
    print(f"Monto total facturado en todo el dia {monto_total_facturado}")

def get_receipt(cliente, subtotal, monto_total_a_pagar):
    print("----------------------------")
    print("----------FACTURA-----------")
    print("----------------------------")
    print()
    print("------SOBRE EL CLIENTE------")
    print(f"Codigo Comprador: {cliente.get('Codigo Comprador')}")
    print(f"Linea De Producto: {cliente.get('Linea De Producto')}")
    print(f"Forma De Pago: {cliente.get('Forma De Pago')}")
    print("----------------------------")
    print("------INFORMACION PAGO------")
    print(f"Subtotal a Pagar: {subtotal}")
    print(f"Total a Pagar: {monto_total_a_pagar}")

def main():
    product_line = {
        "Q": {
            "description": "Quimicos",
            "price": 50
        },
        "F": {
            "description": "Farmaceuticos",
            "price": 100
        }
    }

    payment_method = {
        "C": "Contado",
        "R": "Credito"
    }

    clientes = []

    print("--------------------------")
    print("--------BIENVENIDO--------")
    print("--------------------------")
    print()

    while True:
        cliente = get_client_data(product_line, payment_method)
        clientes.append(cliente)
        subtotal = get_subtotal(cliente)
        IVA = get_IVA(cliente, subtotal)
        monto_total_a_pagar = get_total_amount(subtotal, IVA)
        get_receipt(cliente, subtotal, monto_total_a_pagar)
        cliente["Subtotal a Pagar"] = subtotal
        cliente["IVA"] = IVA
        cliente["Total a Pagar"] = monto_total_a_pagar
        
        keep_adding_client = input(" Que desea realizar? \n 1. Agregar otro cliente \n 2. Salir \n --> ")
        while not keep_adding_client.isnumeric() or not int(keep_adding_client) in range(1, 3):
            keep_adding_client = input(" Ingreso Invalido. Que desea realizar? \n 1. Agregar otro cliente \n 2. Salir \n --> ")
        
        if keep_adding_client == "2":
            break
    get_final_day_status(clientes)

main()