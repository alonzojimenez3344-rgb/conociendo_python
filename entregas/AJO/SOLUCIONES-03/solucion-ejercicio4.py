# Ejercicio 04 — Calificaciones de 5 alumnos (3 cada uno)

for alumno in range(1, 6):
    print(f"Alumno {alumno}:")
    suma = 0

    for i in range(1, 4):
        calificacion = float(input(f"Calificación {i}: "))
        suma = suma + calificacion

    promedio = suma / 3
    print(f"Promedio del alumno {alumno}: {promedio}")
    print()
