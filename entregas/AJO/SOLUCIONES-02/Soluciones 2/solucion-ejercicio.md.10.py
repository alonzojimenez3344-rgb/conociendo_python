# Ejercicio 10 — Menor de dos números

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1 < num2:
    menor = num1
else:
    menor = num2

print(f"El menor es {menor}.")