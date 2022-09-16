puntos = int(input("Cuantos puntos tienes?: "))

if puntos >=1 and puntos <=50:
    print("No hay premios para" + puntos + "pts")
elif puntos >50 and puntos <=150:
    print(f"Felicitaciones, Ganaste la medalla de Bronze por haber tenido {puntos} pts")
elif puntos >150 and puntos <=180:
    print(f"Felicitaciones, Ganaste la medalla de PLata por haber tenido {puntos} pts")
elif puntos >180 and puntos <=200:
    print(f"Felicitaciones, Ganaste la medalla de Oro por haber tenido {puntos} pts")
else:
    print("Error")

print("Fin.")