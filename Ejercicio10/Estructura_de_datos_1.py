#Primer ejercicio -> Agregar nombres 'UNICOS'

nombres = []
while len(nombres) < 10:
    nombre = input("Ingresa un nombre (único): ").strip()
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print(f"El nombre '{nombre}' ya ha sido ingresado. Por favor, ingresa un nombre diferente.")

print("Nombres ingresados:", nombres)

# Segundo ejercicio -> 'ELIMINAR' nombres (3° y ultimo)

if len(nombres) >= 3:
    del nombres[2]  # Eliminar la tercera persona (índice 2)
if len(nombres) > 0:
    del nombres[-1]  # Eliminar la última persona

nombres.sort()
print("Lista después de eliminar y ordenar:", nombres)

# Tercer ejercicio -> Guardar datos en un 'DICCIONARIO'

persona = {
    "nombre": input("Nombre: ").strip(),
    "apellido": input("Apellido: ").strip(),
    "dni": input("DNI: ").strip(),
    "email": input("Email: ").strip(),
    "fecha_nacimiento": input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
}

print("Datos de la persona:", persona)

# Cuarto Ejercicio -> Guardar en 'NOMBRES' y 'DATOS' en un 'DICCIONARIO'

familia = {}

for i in range(1, 5):
    nombre_persona = input(f"Ingrese el nombre de la persona {i}: ").strip()
    familia[nombre_persona] = {
        "nombre": nombre_persona,
        "apellido": input(f"Apellido de {nombre_persona}: ").strip(),
        "dni": input(f"DNI de {nombre_persona}: ").strip(),
        "email": input(f"Email de {nombre_persona}: ").strip(),
        "fecha_nacimiento": input(f"Fecha de nacimiento de {nombre_persona} (DD/MM/AAAA): ").strip()
    }

print("Datos de la familia:")
for nombre, datos in familia.items():
    print(f"{nombre}: {datos}")

# Quinto ejercicio -> almacenar numeros 'n' veces

n = int(input("Ingrese el valor de n: ").strip())
numeros_pares = tuple(i for i in range(2 * n) if i % 2 == 0)

print("Los primeros", n, "números pares son:", numeros_pares)

