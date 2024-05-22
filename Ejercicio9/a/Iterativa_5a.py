# contador 'i'
i = 1

# Usuario que ingresa un número
a = int(input('Ingrese un NÚMERO para ver su tabla de multiplicar: '))

# Bucle 'while' que itera desde 1 hasta 10
while i <= 10:
    # Calculamos el resultado de la multiplicación
    b = a * i
    
    print(f'{a} x {i} = {b}')

    # Incrementamos contador
    i += 1
