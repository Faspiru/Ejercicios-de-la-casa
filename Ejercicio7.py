

Jugador1 = input("Cual es tu nombre?: ") 
Jugador2 = input("Cual es tu nombre?: ")
EleccionJ1 = input("Piedra, Papel o Tijera pa?: " .capitalize())
ELeccionJ2 = input("Piedra, Papel o Tijera pa?: " .capitalize())

if EleccionJ1 == "Piedra" and ELeccionJ2 == "Tijera":
    print(f"{Jugador1} Gana! la Piedra rompe la Tijera")
elif ELeccionJ2 == "Piedra" and EleccionJ1 == "Tijera":
    print(f"{Jugador2} Gana! la Piedra rompe la Tijera")
elif EleccionJ1 == "Piedra" and ELeccionJ2 == "Papel":
    print(f"{Jugador2} Gana! el Papel envuelve la Piedra")
elif ELeccionJ2 == "Piedra" and EleccionJ1 == "Papel":
    print(f"{Jugador1} Gana! el Papel envuelve la Piedra")
elif EleccionJ1 == "Papel" and ELeccionJ2 == "Tijera":
    print(f"{Jugador2} Gana! la tijera rompe el papel")
elif ELeccionJ2 == "Papel" and EleccionJ1 == "Tijera":
    print(f"{Jugador1} Gana! la tijera rompe el papel")
elif EleccionJ1 == ELeccionJ2:
    print("Empate! dale otra ronda pa")

print("Fin.")
