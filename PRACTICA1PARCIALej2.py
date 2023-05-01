def print_welcome():
    print("*** Welcome ***")

def get_option(studies):
    for key,value in studies.items():
        for key_interno, value_interno in value.items():
            print(f"{key} - {value_interno}", end = "")
        print("")
    return input("Please enter a option: ")
    

def get_client_data(study):
    client = {
        "id":input("Please enter the client id: "),
        "age":input("Please enter the client age: "),
        "gender":input("Please enter the client gender M or F: "),
        "study": study
    }
    return client
    
def get_discounts(client, studies,client_number):
    discount = 0
    if client.get("gender") == "F" and int(client.get("age")) > 55:
        discount += studies.get(client.get("study")).get("price") * 0.25
    elif client.get("gender") == "M" and int(client.get("age")) > 65:
        discount += studies.get(client.get("study")).get("price") * 0.25
    
    if client_number % 2 != 0:
        discount += studies.get(client.get("study")).get("price") * 0.02

    return discount

def get_net_amount(client, discount, studies):
    return studies.get(client.get("study")).get("price") - discount


def print_invoice(client, studies, net_amount):
    print('*** RECEIPT ***')
    print("Id card:",client.get("id"))
    print("Age:",client.get("age"))
    print("Gender:",client.get("gender"))
    print("Study:",studies.get(client.get("study")).get("description"))
    client["total"] = net_amount
    print("Net Amout:",net_amount)

def final_day(clients, total_discounts, total_amount, client_number, contU, contR, contT, total_net_amountU, total_net_amountR, total_net_amountT):
    for client in clients:
        for key, value in client.items():
            if key == "study":
                if value == "U":
                    contU += 1
                    total_net_amountU += client.get("total")
                if value == "T":
                    contT += 1
                    total_net_amountT += client.get("total")
                if value == "R":
                    contR += 1
                    total_net_amountR += client.get("total")

    print(f"Cantidad de clientes U: {contU}")
    print(f"Cantidad de clientes T: {contT}") 
    print(f"Cantidad de clientes R: {contR}") 
    print(f"Monto total en descuentos otorgados: {total_discounts}")
    print(f"Monto total neto facturado: {total_amount}")
    print(f"Promedio de pago de todos los clientes: {total_amount/client_number}")
    print(f"Promedio de pago por estudio U: {total_net_amountU/contU}")
    print(f"Promedio de pago por estudio T: {total_net_amountT/contT}")
    print(f"Promedio de pago por estudio R: {total_net_amountR/contR}")

def main():
    studies_dict = {
        "U": {
            "description":"Ultrasonido",
            "price": 8900
        },
        "T": {
            "description":"Tomografia",
            "price": 12640
        },
        "R": {
            "description":"Resonancia",
            "price": 15600
        }
    }
    clients = []
    total_discounts = 0
    total_net_amount = 0
    total_net_amountU = 0
    total_net_amountR = 0
    total_net_amountT = 0
    contU = 0
    contT = 0
    contR = 0
    print_welcome()
            
    while True:
        option = get_option(studies_dict)
        client = get_client_data(option)
        clients.append(client)
        discount = get_discounts(client,studies_dict,len(clients))
        total_discounts += discount
        total = get_net_amount(client,discount,studies_dict)
        total_net_amount += total
        print_invoice(client, studies_dict, total)
        final_day(clients, total_discounts, total_net_amount, len(clients), contU, contT, contR, total_net_amountU, total_net_amountT, total_net_amountR)
        if input("Do you want to continue Y-Yes or N-No ") == "N":
            break
    

main()