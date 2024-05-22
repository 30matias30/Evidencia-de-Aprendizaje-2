# Se solicita un número
a = int(input('Ingrese UN número: '))

# Bucle 'FOR' que itera desde 0 hasta el 'a'
for i in range(0, a + 1):
    # Se verifica si 'i' es par y diferente de 0
    if i % 2 == 0 and i != 0:
        print(i)
