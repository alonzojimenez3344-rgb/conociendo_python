A# Ejercicio 02 — Salario neto del obrero

Un obrero trabaja 8 horas diarias por quincena y le pagan a 50 pesos la hora.
De su salario tiene una compensación del 2 % y un descuento del 1.5 % del IMSS
y 1.2 % del ISPT. Realiza un programa que permita calcular el salario neto del
trabajador.

## Datos del problema

| Concepto | Valor |
|----------|-------|
| Horas diarias | 8 |
| Días por quincena | 15 |
| Pago por hora | 50 pesos |
| Compensación | +2 % |
| Descuento IMSS | −1.5 % |
| Descuento ISPT | −1.2 % |

## Ejemplo de salida

```batch
Salario bruto: 6000.00
Compensación: 120.00
Descuento IMSS: 90.00
Descuento ISPT: 72.00
Salario neto: 5958.00
```


## Pista

Calcula el bruto como `8 * 15 * 50` y aplica los porcentajes sobre ese bruto.

## Entrega

`entregas//<tu-usuario>/02_estructura_de_control/ejercicio_02.py`