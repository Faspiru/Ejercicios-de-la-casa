def get_costumer_information():
    print("-----ABOUT COSTUMER-----")

    tipos_de_pago = {
        "1": "Tarjeta",
        "2": "Efectivo" 
    }

    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        nombre = input("Ingreso Invalido. Ingrese su nombre: ")
  
    apellido = input("Ingrese su apellido: ")
    while not apellido.isalpha():
        apellido = input("Ingreso Invalido. Ingrese su nombre: ")
    
    cedula = input("Ingrese su cedula: ")
    while not cedula.isnumeric() or not len(cedula) == 8:
        apellido = input("Ingreso Invalido. Ingrese su cedula: ")

    pagamento = input(" 1. Tarjeta \n 2. Efectivo \n Ingrese su tipo de pago: ")
    while not pagamento.isnumeric() or not int(pagamento) in range(1, 3):
        pagamento = input(" 1. Tarjeta \n 2. Efectivo \n Ingreso Invalido. Ingrese su tipo de pago: ")
    
    cliente = {
        "nombre": nombre,
        "apellido": nombre,
        "cedula": cedula,
        "Tipo de pago": tipos_de_pago.get(pagamento)
    }
    
    return cliente

def add_to_basket(menu):
    basket = []
    
    while True:
        print("Seleccion de productos -->")
        for i, product in enumerate(menu):
            print(f"{i+1} {product.get('name')} {product.get('price')}$")
        
        eleccion_de_compra = input("Ingrese el numero del producto que desea comprar: ")
        while not eleccion_de_compra.isnumeric() or  not int(eleccion_de_compra) in range(1, 5):
            eleccion_de_compra = input("Ingreso Invalido. Ingrese el numero del producto que desea comprar: ")

        basket.append(menu[int(eleccion_de_compra)-1])
        
        continue_adding = input("Desea seguir agregando productos al carrito? \n 1. SI \n 2. NO \n --> ")
        while not continue_adding.isnumeric() or not int(continue_adding) in range(1,3):
            continue_adding = input("Ingreso Invalido, desea seguir agregando productos al carrito? \n 1. SI \n 2. NO \n --> ")
        if continue_adding == "2":
            break
    
    return basket

def calculate_subtotal(basket):
    subtotal = 0
    for product in basket:
        subtotal += product.get("price")
    return subtotal

def calculate_tax(subtotal):
    tax = subtotal * 0.16
    total_with_tax = subtotal - tax
    return total_with_tax

def get_receipt(cliente, basket, subtotal, total_with_tax):
    print("-------- FACTURA --------")
    print("CLIENTE")
    print(f"Nombre: {cliente.get('nombre')} {cliente.get('apellido')}")
    print(f"Cedula: {cliente.get('cedula')}")
    print(f"Tipo De Pago: {cliente.get('Tipo de pago')}")
    print("-------------------------")
    print("PRODUCTOS")
    for product in basket:
        print(f"{product.get('name')} {product.get('price')}$")
    print("-------------------------")
    print(f"Subtotal: {subtotal}$")
    print(f"Total: {round(total_with_tax, 2)}")

def main():
    menu = [
        {
      "name": "Manzana",
      "price": 1.15
    },
    {
      "name": "Aguacate",
      "price": 2.5
    },
    {
      "name": "Malta",
      "price": 1.05
    },
    {
      "name": "Pan",
      "price": 2.0
    }
    ]

    cliente = get_costumer_information()
    #print(cliente)
    basket = add_to_basket(menu)
    subtotal = calculate_subtotal(basket)
    total_with_tax = calculate_tax(subtotal)
    get_receipt(cliente, basket, subtotal, total_with_tax)

main()
