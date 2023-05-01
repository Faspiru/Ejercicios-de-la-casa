def get_costumer_information():
  print("-----ABOUT COSTUMER-----")

  nombre = input("Ingrese su nombre: ")
  while not nombre.isalpha():
    nombre = input("Ingreso Invalido. Ingrese su nombre: ")
  
  apellido = input("Ingrese su apellido: ")
  while not apellido.isalpha():
    apellido = input("Ingreso Invalido. Ingrese su nombre: ")






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
  




main()