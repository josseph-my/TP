# sistema de gestion de estudiantes basado en sistema CRUD

# Ingreso de usuario
varNombreUsuario = input("Ingrese su usuario: ")
varCodigoUsuario = input("Ingrese su codigo: ")
varUsuario = [varNombreUsuario, varCodigoUsuario]

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
        RegistrarEstudiante()
    elif varOpcion == "2":
        MostrarEstudiantes()
    elif varOpcion == "3":
        BuscarEstudiante()
    elif varOpcion == "4":
        ActualizarEstudiante()
    elif varOpcion == "5":
        EliminarEstudiante()
    elif varOpcion == "6":
        print("Ha salido del menu")
    else:
        print("Opción inválida. Intente nuevamente.")
        menu()
