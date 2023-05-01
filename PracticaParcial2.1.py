def get_student_data():
    cedula = input("Ingrese su cedula: ")
    while not cedula.isnumeric():
        cedula = input("Ingreso Invalido. Ingrese su cedula: ")
    
    promedio_notas = input("Ingrese su promedio de notas durante educacion primaria y media: ")
    while promedio_notas.isalpha() or not int(promedio_notas) in range(0, 21):
        promedio_notas = input("Ingreso Invalido. Ingrese su promedio de notas durante educacion primaria y media: ")
    promedio_notas = float(promedio_notas)

    trimestre = ""
    if promedio_notas >= 18:
        trimestre = "A"
    elif promedio_notas >= 12:
        trimestre = "B"
    elif promedio_notas <12:
        trimestre = "Rechazado"

    estudiante = {
        "Cedula": cedula,
        "Promedio de Notas": promedio_notas,
        "Trimestre Asignado": trimestre
    }
    return estudiante

def print_student_data(estudiante):
    print("---------------------------")
    print("------DATOS OBTENIDOS------")
    print("---------------------------")
    print()
    print(f"Cedula: {estudiante.get('Cedula')}")
    print(f"Promedio de Notas: {estudiante.get('Promedio de Notas')}")
    print(f"Trimestre Asignado: {estudiante.get('Trimestre Asignado')}")

def final_day_status(estudiantes, cont_estudiantes, estudiantesB, estudiantesA):
    contA = 0
    contB = 0
    contR = 0
    promedioA = 0
    promedioB = 0

    for estudiante in estudiantes:
        if estudiante.get("Trimestre Asignado") == "A":
            contA += 1
            promedioA += estudiante.get("Promedio de Notas")
        if estudiante.get("Trimestre Asignado") == "B":
            contB += 1
            promedioB += estudiante.get("Promedio de Notas")
        if estudiante.get("Trimestre Asignado") == "Rechazado":
            contR += 1

    print("---------------------------")
    print("-------DATOS FINALES-------")
    print("---------------------------")
    print()
    print(f"Cantidad de alummos aspirantes: {cont_estudiantes}")
    print(f"Cantidad de alumnos al trimestre A: {contA}")
    print(f"Cantidad de alumnos al trimestre B: {contB}")
    print(f"Cantidad de alumnos rechazados: {contR}")
    print("Promedio de aspirantes trimestre A")
    for i, estudianteA in enumerate(estudiantesA):
        print(f"{i+1}. promedio: {estudianteA.get('Promedio de Notas')}")
    print("Promedio de aspirantes trimestre B")
    for i, estudianteB in enumerate(estudiantesB):
        print(f"{i+1}. promedio: {estudianteB.get('Promedio de Notas')}")
    print(f"Promedio general del trimestre A: {promedioA/contA}")
    print(f"Promedio general del trimestre B: {promedioB/contB}")

    


def main():
    print()
    print("-------BIENVENIDO-------")
    print()
    
    estudiantes = []
    estudiantesA = []
    estudiantesB = []

    while True:
        estudiante = get_student_data()
        estudiantes.append(estudiante)
        if estudiante.get("Trimestre Asignado") == "A":
            estudiantesA.append(estudiante)
        if estudiante.get("Trimestre Asignado") == "B":
            estudiantesB.append(estudiante)
        print_student_data(estudiante)
       
        keep_adding_students = input(" Que desea realizar? \n 1. Agregar Estudiante \n 2. Salir \n --> ")
        while not keep_adding_students.isnumeric() or not int(keep_adding_students) in range(1, 3):
            keep_adding_students = input(" Ingreso Invalido. Que desea realizar? \n 1. Agregar Estudiante \n 2. Salir \n --> ")
        if keep_adding_students == "2":
            break
    final_day_status(estudiantes, len(estudiantes), estudiantesB, estudiantesA)

main()