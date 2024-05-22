a = int(input('Ingrese un NÚMERO para ver su tabla de multiplicar: '))

# Bucle 'for' que itera desde 1 hasta 10 (inclusive)
for i in range(1, 11):
    # Resultado de la multiplicación
    b = a * i
    
    print(f'{a} x {i} = {b}')
