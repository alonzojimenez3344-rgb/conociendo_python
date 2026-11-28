# Ejercicio 09 — Salario con horas extra

horas = float(input("Horas trabajadas: "))

if horas <= 40:
    salario = horas * 50
else:
    salario = 40 * 50 + (horas - 40) * 70

print(f"Horas trabajadas: {horas}")
print(f"Salario: {salario}")