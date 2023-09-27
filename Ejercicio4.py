lista_alumnos = []

numero_alumnos = int(input("Ingrese la cantidad de alumnos a registrar: "))
for i in range(numero_alumnos):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    # Calificaciones del alumno
    notas_alumno = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} del alumno {nombre_alumno}: "))
        notas_alumno.append(nota)  
    #Diccionario con los datos del alumno
    alumno = {
        "Alumno": nombre_alumno,
        "Notas": notas_alumno
    }
    lista_alumnos.append(alumno)
#Listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"Alumno: {alumno['Alumno']}")
    print(f"Notas: {alumno['Notas']}")
    print()
