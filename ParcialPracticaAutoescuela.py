def get_client_data():
    cedula = input("Ingrese su cedula: ")
    while not cedula.isnumeric():
        cedula = input("Ingreso Invalido. Ingrese su cedula: ")
    
    tipo_de_vehiculo = input("Ingrese el tipo del vehiculo \n A. Automatico \n S. Sincronico \n -->  ").upper()
    while not tipo_de_vehiculo.isalpha() or not tipo_de_vehiculo == "A" and not tipo_de_vehiculo == "S":
        tipo_de_vehiculo = input("Ingreso Invalido. Ingrese el tipo del vehiculo \n A. Automatico \n S. Sincronico \n -->  ")

    numero_horas = input("Cuantas horas va a tomar?: ")
    while not numero_horas.isnumeric():
        numero_horas = input("Ingreso Invalido. Ingrese cuantas horas va a tomar")
    numero_horas = int(numero_horas)

    cliente = {
        "Cedula": cedula,
        "Tipo de Vehiculo": tipo_de_vehiculo,
        "Horas a tomar": numero_horas
    }
    return cliente

def get_subtotal(cliente, vehiculos_dict):
    subtotal = 0
    subtotal += (vehiculos_dict.get(cliente.get("Tipo de Vehiculo")).get("price/hour") * cliente.get("Horas a tomar"))
    return subtotal

def get_discount(cliente, subtotal):
    discount = 0
    if cliente.get("Horas a tomar") > 3:
        discount += subtotal * 0.15
    return discount

def get_total(discount, subtotal):
    total = subtotal - discount
    return total


def get_receipt(cliente, vehiculos_dict, total, discount):
    print("--------FACTURA--------")
    print(f"Cedula: {cliente.get('Cedula')}")
    print(f"Tipo de Vehiculo: {vehiculos_dict.get(cliente.get('Tipo de Vehiculo')).get('description')}")
    print("-----------------------")
    print(f"Monto total: {total}")
    print(f"Descuento otorgado: {discount}")

def get_final_day_data(clientes, num_clientes):
    contA = 0
    contS = 0
    contCD = 0 
    pago_automaticos = 0
    pago_sincronicos = 0
    for cliente in clientes:
        if cliente.get("Tipo de Vehiculo") == "A":
            contA += 1
            pago_automaticos += cliente.get("Monto Total a Pagar")
        if cliente.get("Tipo de Vehiculo") == "S":
            contS += 1
            pago_sincronicos += cliente.get("Monto Total a Pagar")
        if cliente.get("Descuento Otorgado") != 0:
            contCD += 1

    print("------FINAL DAY------")
    print(f"Numero total de clientes: {num_clientes}")
    print(f"Clientes totales para vehiculos Automaticos: {contA}")
    print(f"Clientes totales para vehiculos Sincronicos: {contS}")
    print(f"Clientes totales con descuento: {contCD}")
    if contA == 0:
        print("No hay pagos en Automatico")
    else:
        print(f"Promedio de facturacion en vehiculos automaticos: {pago_automaticos/contA}")
    if contS == 0:
        print("No hay pagos en Sincronico")
    else:
        print(f"Promedio de facturacion en vehiculos sincronicos: {pago_sincronicos/contS}")
    
def main():
    vehiculos_dict ={
        "A": {
            "description": "Automatico",
            "price/hour": 2500
        },
        "S": {
            "description": "Sincronico",
            "price/hour": 3500
        }
    }

    clientes = []

    while True:
        print("------BIENVENIDO------")
        print()
        cliente = get_client_data()
        clientes.append(cliente)
        subtotal = get_subtotal(cliente, vehiculos_dict)
        discount = get_discount(cliente, subtotal)
        total = get_total(discount, subtotal)
        get_receipt(cliente, vehiculos_dict, total, discount)
        cliente["Descuento Otorgado"] = discount
        cliente["Monto Total a Pagar"] = total

        keep_adding_clients = input("Que desea realizar? \n 1. Agregar otro cliente \n 2. Salir \n --> ")
        while not keep_adding_clients.isnumeric() or not int(keep_adding_clients) in range (1, 3):
            keep_adding_clients = input("Ingreso Invalido. Que desea realizar? \n 1. Agregar otro cliente \n 2. Salir \n --> ")
        
        if keep_adding_clients == "2":
            break
    get_final_day_data(clientes, len(clientes))
main()