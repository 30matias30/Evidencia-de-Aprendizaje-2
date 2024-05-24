def show_menu():
    print("\nMenu de opciones:")
    print("1-> Agregar una persona")
    print("2-> Modificar una persona")
    print("3-> Eliminar una persona")
    print("4-> Mostrar toda la agenda")
    print("5-> Salir")

# Agregar Persona

def agregar_persona(agenda):
    dni = input("Ingrese el DNI: ").strip()
    if dni in agenda:
        print("La persona con este DNI ya existe.")
    else:
        apellido = input("Ingrese el apellido: ").strip()
        nombre = input("Ingrese el nombre: ").strip()
        email = input("Ingrese el email: ").strip()
        telefono = input("Ingrese el número de teléfono: ").strip()
        agenda[dni] = {
            "apellido": apellido,
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        print("Persona agregada con éxito.")

# Modificar Persona

def modificar_persona(agenda):
    dni = input("Ingrese el DNI de la persona a modificar: ").strip()
    if dni in agenda:
        print(f"Datos actuales: {agenda[dni]}")
        cambiar = input("¿Desea cambiar el apellido? (y/n): ").strip().lower()
        if cambiar == 'y':
            agenda[dni]['apellido'] = input("Ingrese el nuevo apellido: ").strip()
        
        cambiar = input("¿Desea cambiar el nombre? (y/n): ").strip().lower()
        if cambiar == 'y':
            agenda[dni]['nombre'] = input("Ingrese el nuevo nombre: ").strip()
        
        cambiar = input("¿Desea cambiar el email? (y/n): ").strip().lower()
        if cambiar == 'y':
            agenda[dni]['email'] = input("Ingrese el nuevo email: ").strip()
        
        cambiar = input("¿Desea cambiar el número de teléfono? (y/n): ").strip().lower()
        if cambiar == 'y':
            agenda[dni]['telefono'] = input("Ingrese el nuevo número de teléfono: ").strip()
        
        print("Datos modificados con éxito.")
    else:
        print("No se encontró una persona con ese DNI.")

# Eliminar Persona

def eliminar_persona(agenda):
    dni = input("Ingrese el DNI de la persona a eliminar: ").strip()
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada con éxito.")
    else:
        print("No se encontró una persona con ese DNI.")

# Mostrar Agenda

def mostrar_agenda(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        for dni, datos in agenda.items():
            print(f"DNI: {dni}, Datos: {datos}")

# Menú Principal -> LLamar Funciones 

def main():
    agenda = {}
    while True:
        show_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            agregar_persona(agenda)
        elif opcion == '2':
            modificar_persona(agenda)
        elif opcion == '3':
            eliminar_persona(agenda)
        elif opcion == '4':
            mostrar_agenda(agenda)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
