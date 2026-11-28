horas_diarias = 8
dias_quincena = 15
pago_hora = 50.0

salario_bruto = horas_diarias * dias_quincena * pago_hora
compensacion = salario_bruto * 0.02
descuento_imss = salario_bruto * 0.015
descuento_ispt = salario_bruto * 0.012

salario_neto = salario_bruto + compensacion - descuento_imss - descuento_ispt

print(f"Salario bruto: {salario_bruto:.2f}")
print(f"Compensación: {compensacion:.2f}")
print(f"Descuento IMSS: {descuento_imss:.2f}")
print(f"Descuento ISPT: {descuento_ispt:.2f}")
print(f"Salario neto: {salario_neto:.2f}")