# Inicializamos la variable i
i = 0

print('Ingrese nombres - Para finalizar, ingrese FIN.')

# Primer nombre
a = input()

# Bucle que verifica si el nombre NO es 'fin'
while a.lower() != 'fin':
    i += 1
    print('Ingrese otro:')
    a = input()

#  Total de valores ingresados
print('Total de valores ingresados:', i)
