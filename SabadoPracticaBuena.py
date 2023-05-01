def get_client_data(studies_dict):
    
    tipo_de_estudio_dict_interno = {
        "1": "U",
        "2": "T",
        "3": "R"
    }

    cedula = input("Ingrese su cedula: ")
    while not cedula.isnumeric() or not len(cedula) == 8:
        cedula = input("Ingreso Invalido. Ingrese su cedula: ")

    edad = input("Ingrese su edad: ")
    while not edad.isnumeric():
        edad = input("Ingreso Invalido. Ingrese su edad: ")
    edad = int(edad)
    
    sexo = input("Ingrese su sexo, (M o F): ").upper()
    while not sexo.isalpha() or not sexo == "M" and not sexo == "F":
        sexo = input("Ingreso Invalido. Ingrese su sexo: ").upper()

    estudio = input("Ingrese que tipo de estudio desea \n 1. Ultrasonido \n 2. Tomografia \n 3. Resonancia \n --> ")
    while not estudio.isnumeric() or not int(estudio) in range(1, 4):
        estudio = input("Ingreso Invalido. Ingrese que tipo de estudio desea \n 1. Ultrasonido \n 2. Tomografia \n 3. Resonancia \n --> ")

    cliente = {
        "Cedula": cedula,
        "Edad": edad,
        "Sexo": sexo,
        "Estudio Key": tipo_de_estudio_dict_interno.get(estudio),
        "Estudio": studies_dict.get(tipo_de_estudio_dict_interno.get(estudio)).get("Description")
    }

    return cliente

def get_discount(cliente, studies_dict):
    discount = 0
    if cliente.get("Sexo") == "F" and cliente.get("Edad") > 55:
        discount = studies_dict.get(cliente.get("Estudio Key")).get("price") * 0.25
    if cliente.get("Sexo") == "M" and cliente.get("Edad") > 65:
        discount = studies_dict.get(cliente.get("Estudio Key")).get("price") * 0.25

    total_with_first_discount = studies_dict.get(cliente.get("Estudio Key")).get("price") - discount

    return total_with_first_discount

def get_aditional_discount(total_with_first_discount, client_number):
    if client_number%2 != 0:
        discount_aditional = 0
        discount_aditional += total_with_first_discount * 0.02
        total_with_second_discount = total_with_first_discount - discount_aditional
    else:
        total_with_second_discount = total_with_first_discount

    return total_with_second_discount

def get_receipt(cliente, total_with_second_discount):
    factura = {
        "Cedula": cliente.get('Cedula'),
        "Edad": cliente.get('Edad'),
        "Sexo": cliente.get('Sexo'),
        "Tipo De Estudio": cliente.get('Estudio'),
        "Monto Total a Pagar": total_with_second_discount
    }
    print("--------FACTURA--------")
    print(f"Cedula: {cliente.get('Cedula')}")
    print(f"Edad: {cliente.get('Edad')}")
    print(f"Sexo: {cliente.get('Sexo')}")
    print(f"Tipo De Estudio: {cliente.get('Estudio')}")
    print(f"Monto Total a Pagar: {total_with_second_discount}")
    return factura

def get_final_day_status(clientes, studies_dict, client_number):
    contU = 0
    contT = 0
    contR = 0
    descuentos_totales = 0
    total_facturado = 0
    total_facturadoU = 0
    total_facturadoT = 0
    total_facturadoR = 0

    for cliente in clientes:
        if cliente.get("Estudio Key") == "U":
            contU += 1
            total_facturadoU += cliente.get("Total a Pagar")
        elif cliente.get("Estudio Key") == "T":
            contT += 1
            total_facturadoT += cliente.get("Total a Pagar")
        elif cliente.get("Estudio Key") == "R":
            contR += 1
            total_facturadoR += cliente.get("Total a Pagar")

    for cliente in clientes:
        descuentos_totales += ((studies_dict.get(cliente.get("Estudio Key")).get("price")) - cliente.get("Total a Pagar"))
        total_facturado += cliente.get("Total a Pagar")
    

    print()
    print("-------FINAL STATUS-------")
    print()
    print(f"Cantidad de clientes en Ultrasonido: {contU}")
    print(f"Cantidad de clientes en Tomografia: {contT}")
    print(f"Cantidad de clientes en Resonancia: {contR}")
    print("-----------------------------------------")
    print(f"Descuentos Totales: {descuentos_totales}")
    print("-----------------------------------------")
    print(f"Monto Total Neto Facturado: {total_facturado}")
    print(f"Promedio de pago: {total_facturado/client_number}")
    print("-----------------------------------------")
    print(f"Promedio de pago en Ultrasonido: {total_facturadoU/contU}")
    print(f"Promedio de pago en Tomografia: {total_facturadoT/contT}")
    print(f"Promedio de pago en Resonancia: {total_facturadoR/contR}")


def main():
    studies_dict = {
        "U": {
            "Description": "Ultrasonido",
            "price": 8900
        },
        "T": {
            "Description": "Tomografia",
            "price": 12640
        },
        "R": {
            "Description": "Resonancia",
            "price": 15600
        }
    }

    clientes = []
    
    while True:
        print("--------WELCOME--------")
        cliente = get_client_data(studies_dict)
        clientes.append(cliente)
        total_with_first_discount = get_discount(cliente, studies_dict)
        total_with_second_discount = get_aditional_discount(total_with_first_discount, len(clientes))
        get_receipt(cliente, total_with_second_discount)
        cliente["Total a Pagar"] = total_with_second_discount
        keep_adding_client = input(" 1. Salir \n 2. Agregar Cliente \n Que desea realizar --> ")
        while not keep_adding_client.isnumeric() or not int(keep_adding_client) in range (1, 3):
            keep_adding_client = input(" 1. Salir \n 2. Agregar Cliente \n Ingreso Invalido. Que desea realizar --> ")
        if keep_adding_client == "1":
            break
    get_final_day_status(clientes, studies_dict, len(clientes))


main()