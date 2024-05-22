# Constante TotalEstudiantes
TE = 5

# Acumulador de notas
b = 0

# Bucle 'for' que itera desde 1 hasta TE (inclusive)
for i in range(1, TE + 1):
    # Solicitamos la nota del alumno
    a = float(input(f'Ingrese la nota del alumno {i}: '))
    # Acumulamos la nota en b
    b += a

# Calculamos el promedio
p = b / TE

# Rendimiento del curso
if p > 8:
    print('El rendimiento del curso ha sido ELEVADO.')
    print('Promedio de', p)
elif p >= 6:
    print('El rendimiento del curso ha sido ACEPTABLE.')
    print('Promedio de', p)
else:
    print('El rendimiento del curso ha sido BAJO.')
    print('Promedio de', p)
