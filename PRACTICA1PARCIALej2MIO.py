def welcome():
    print("********** WELCOME **********")

def get_option(studies):
    for key, value in studies.items():
        description = value.get("description")
        price = value.get("price")
        print(f"{key} --- {description} --- {price}")
    client_option_decision = input("PLease enter a valid option (U, T or R): ").upper()
    return client_option_decision

def get_client_data(study):
    client = {
        "id" : input("PLease enter your id: "),
        "age" : int(input("PLease enter your age: ")),
        "gender" : input("PLease enter your gender (M or F): "),
        "study": study
    }
    return client

def get_discount(client, studies, client_number):
    discount = 0 
    if client.get("gender") == "F" and client.get("age") > 55:
        discount += studies.get(client.get("study")).get("price") * 0.25
    elif client.get("gender") == "M" and client.get("age") > 65:
        discount += studies.get(client.get("study")).get("price") * 0.25

    if client_number%2 != 0:
        discount += studies.get(client.get("study")).get("price") * 0.02

    return discount

def get_net_amount(studies, client, discount):
    return studies.get(client.get("study")).get("price") - discount

def get_receipt(client, studies, net_amount):
    print("****** RECEIPT ******")
    print(f"id card: {client.get('id')}")
    print(f"age: {client.get('age')}")
    print(f"gender: {client.get('gender')}")
    print(f"study: {studies.get(client.get('study')).get('description')}")
    client["total"] = net_amount
    print(f"net amount: {net_amount}")


def main():
    studies_dict = {
        "U": {
        "description" : "Ultrasonido",
        "price": 8900
        }, 
        "T": {
            "description": "Tomografia",
            "price": 12640
        }, 
        "R": {
            "description": "Resonancia", 
            "price": 15600
        }
    }

    clients = []
    total_discount = 0 
    total_net_amount = 0

    welcome()
    while True:
        option = get_option(studies_dict)
        client = get_client_data(option)
        clients.append(client)
        discount = get_discount(client, studies_dict,len(clients))
        total_discount += discount
        total = get_net_amount(studies_dict, client, discount)
        total_net_amount += total
        get_receipt(client, studies_dict, total_net_amount)
        if input("Desea continuar o salir?: ").upper() == "S":
            break

main()
    