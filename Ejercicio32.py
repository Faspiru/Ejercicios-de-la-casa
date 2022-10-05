contra = input("Ingrese una contrasena valida: ")

cont_mayus = 0
cont_minus = 0

while contra.isalnum() or contra.isnumeric() or contra.isalpha() or not len(contra) == 8 or cont_mayus==0 or cont_minus==0:
    contra = input("La contrasena debe contener 8 caracteres, ademas almenos una letra, un numero, un caracter especial, una Mayus y una Minus: ")
    cont_mayus = 0
    cont_minus = 0 
    for i in contra:
        if i.isupper():
            cont_mayus += 1 
        elif i.islower():
            cont_minus += 1
    print(cont_mayus)
    print(cont_minus)
    
  