# Ejercicio 05 — Aceptar solo calificaciones entre 6 y 10

contador = 1

while contador <= 10:
    calificacion = float(input(f"Calificación {contador}: "))

    if calificacion >= 6 and calificacion <= 10:
        print("→ Aceptada.")
        contador = contador + 1
    else:
        print("→ Inválida, intenta de nuevo.")
