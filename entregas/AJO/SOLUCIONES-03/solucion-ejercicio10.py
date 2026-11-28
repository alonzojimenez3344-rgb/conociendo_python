# Ejercicio 10 — Suma de los cuadrados de los 100 primeros enteros

suma = 0

for i in range(1, 101):
    suma = suma + i * i

print(f"La suma de los cuadrados del 1 al 100 es {suma}.")