# sistema de gestion de estudiantes basado en CRUD

# Mostrar las opciones a escoger


def menu():
    print("\nMenu de opciones")
    print("1-Registrar estudiante")
    print("2-Mostrar estudiantes")
    print("3-Buscar estudiante")
    print("4-Actualizar información")
    print("5-Eliminar estudiante")
    print("6-Salir")

    # Selección y funciones según la opción escogida

    varOpcion = input("Seleccione el número de opción: ")

    if varOpcion == "1":
        registrar_estudiante()
    elif varOpcion == "2":
        mostrar_estudiantes()
    elif varOpcion == "3":
        buscar_estudiante()
    elif varOpcion == "4":
        actualizar_estudiante()
    elif varOpcion == "5":
        eliminar_estudiante()
    elif varOpcion == "6":
        print("Ha salido del menu")
    else:
        print("Opción inválida. Intente nuevamente.")
        menu()


# variable de lista que se basaran los procesos
varLista_Estudiantes = []


# Proceso para actualización de estudiantes


def actualizar_estudiante():
    varCodigo = input(
        "Ingrese el código del estudiante que desea actualizar: ")
    for est in varLista_Estudiantes:
        if est["codigo"] == varCodigo:
            print("Ingrese los nuevos datos o deje en blanco para no cambiar:")
            varNuevo_Nombre = input(
                f"Nuevo nombre ({est['nombre']}): ") or est["nombre"]
            varNueva_Edad = input(
                f"Nueva edad ({est['edad']}): ") or est["edad"]
            varNueva_Carrera = input(
                f"Nueva carrera ({est['carrera']}): ") or est["carrera"]
            varNuevo_Promedio = input(
                f"Nuevo promedio ({est['promedio']}): ") or est["promedio"]

            # Restricciones de numeros negativos y promedios fuera de rango
            if not varNuevo_Nombre.isdigit() or int(varNueva_Edad) <= 0:
                print("Edad invalida")
                return
            if not varNuevo_Promedio.replace(".", "").isdigit() or not (0 <= float(varNuevo_Promedio) <= 100):
                print("Promedio invalido")
                return


# Ejecutar
menu()
