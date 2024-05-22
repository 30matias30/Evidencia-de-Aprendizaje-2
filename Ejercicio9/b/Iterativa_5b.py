# contador 'i'
i = 1

# número
a = int(input('Ingrese un NÚMERO para ver su tabla de multiplicar: '))

# Bucle que itera hasta que i sea 'MAYOR' que 10
while i <= 10:
    # Calculamos la multiplicación
    b = a * i
    
    print(f'{a} x {i} = {b}')

    # Incrementamos i
    i += 1
