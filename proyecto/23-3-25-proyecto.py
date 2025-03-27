# sistema de gestion de estudiantes basado en sistema CRUD

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


# variable de lista que almacena los estudiantes y sus datos
varEstudiantes = []

# registrar estudiantes


def RegistrarEstudiante():

    varCodigo = int(input("Ingrese el codigo del estudiante: "))

    # Comprabar que el codigo no este registrado
    for est in varEstudiantes:
        if est[varCodigo] == varCodigo:
            print("Codigo ya registrado.")
            return
    varNombre = input("Ingrese el nombre del estudiante: ")
    varEdad = int(input("Ingrese la edad del estudiante: "))
    varCarrera = input("Ingrese la carrera del estudiante: ")
    varPromedio = float(input("Ingrese el promedio de estudiante: "))

    # Comprabar que el promedio este dentro del rango 0-100
    if varPromedio < 0 or varPromedio > 100:
        print("Promedio invalido. Ingrese un promedio entre 0-100")
        return

    # Tomar los datos de entrada anteriores y colocarlos en una variable diccionario del estudiante
    varEstudiantes.append({
        'codigo': varCodigo,
        'nombre': varNombre,
        'edad': varEdad,
        'carrera': varCarrera,
        'promedio': varPromedio
    })

    print("\n" * 2, "***Estudiante registrado correctamente***", "\n" * 2)
    menu()

# mostrar estudiantes


def MostrarEstudiantes():
    for est in varEstudiantes:
        print("\n" * 2)
        print(
            f"Código: {est['codigo']}, Nombre: {est['nombre']}, Edad: {est['edad']},Carrera: {est['carrera']}, Promedio: {est['promedio']}")
        print("\n" * 2)
    menu()

# Proceso para actualización de estudiantes


def ActualizarEstudiante():
    varCodigo = input(
        "Ingrese el código del estudiante que desea actualizar ")
    for est in varEstudiantes:
        if est['codigo'] == varCodigo:
            print("Ingrese los nuevos datos ")
            varNuevoNombre = input(
                f"Nuevo nombre ({est['nombre']}): ")
            varNuevaEdad = int(input(
                f"Nueva edad ({est['edad']}): "))
            varNuevaCarrera = input(
                f"Nueva carrera ({est['carrera']}): ")
            varNuevoPromedio = input(
                f"Nuevo promedio ({est['promedio']}): ")

            # Comprobar que el promedio esta en rango 0-100
            if varNuevoPromedio < 0 or varNuevoPromedio > 100:
                print("Promedio invalido. Ingrese un promedio entre 0-100")
                return
    menu()


menu()
