import random

def generate_tickets():
    while True:
        try:
            numero = int(input("Ingrese un numero natural: "))
            if numero == 0:
                raise Exception
            break
        except ValueError:
            print("Revisa tu tipo de dato")
        except IndentationError:
            print("Revisa tus margenes")
        except:
            print("Error desconocido")
    tickets = []

    while len(tickets) < numero:
        t = random.randint(10000000, 99999999)
        if t not in tickets:
            tickets.append(t)
    print(tickets)
    return tickets 

def choice_winner(lista_tickets):
    winner = random.choice(lista_tickets)
    return winner


def main():
    lista_tickets = generate_tickets()
    ganador = choice_winner(lista_tickets)
    print(f"El Ticket ganador es: {ganador}")
main()