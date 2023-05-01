def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range (2, num):
        if num % x == 0:
            return False
    return True

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

def main():
    numero = input("Dime un numero: ")
    numero = int(numero)
    es_prime = is_prime(numero)
    print(es_prime)

main()