# Constante para el valor de los m2
VALOR_M2 = 1000

# Largo de la pared
l = float(input('Introduce el LARGO de la pared: '))

# Alto de la pared
a = float(input('Introduce el ALTO de la pared: '))

# Calculamos
# Metros cuadrados y precio
m2 = a * l
precio = m2 * VALOR_M2

# Presupuesto
print('El PRESUPUESTO para la pared de', m2, 'metros cuadrados')
print('es de $', precio)
