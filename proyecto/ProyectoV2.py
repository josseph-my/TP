# sistema de gestion de estudiantes basado en sistema CRUD

# Variable global de estudiantes
varListaEstudiante = []

# Ingreso de usuario log in


def login():
    listaUsuario = []
    listaContraseña = []
    while True:
        varSiONo = input("¿Ya tiene un usuario registrado?, ¿Si o No? ")
        if varSiONo.lower() == "no":

            varUsuarioNuevo = input("Ingrese el usuario que quiere utilizar: ")
            listaUsuario.append(varUsuarioNuevo)
            varContraseñaNueva = input(
                "Ingrese la contraseña que va a utilizar: ")
            listaContraseña.append(varContraseñaNueva)

            print("Usuario registrado correctamente")
            print("Ingrese su usuario y contraseña")

            varUsuario = input("Usuario: ")
            varContraseña = input("Contraseña: ")

            if varUsuario == listaUsuario[0] and varContraseña == listaContraseña[0]:
                print("Bienvenido")
                break
            else:
                print("Usuario o contraseña incorrectos")

        elif varSiONo == "si":
            print("Ingrese su usuario y contraseña")

            varUsuario = input("Usuario: ")
            varContraseña = input("Contraseña: ")

            if varUsuario == listaUsuario[0] and varContraseña == listaContraseña[0]:
                print("Bienvenido")
                break
            else:
                print("Usuario o contraseña incorrectos")
        else:
            print("Opcion invalida, intente otra vez")

# Mostrar las opciones del menu principal


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


def VolverMenu():
    varVolver = input("Desea volver al menu ")
    if varVolver.lower() == "si":
        menu()
    else:
        print("Ha salido del menu ")


def RegistrarEstudiante():
    varEstudiante = []
    varNombre = input("Ingrese el nombre del estudiante: ")
    varEstudiante.append(varNombre)
    varCodigo = int(input("Ingrese el codigo del estudiante: "))
    varEstudiante.append(varCodigo)
    varEdad = int(input("Ingrese la edad del estudiante: "))
    varEstudiante.append(varEdad)
    varCarrera = input("Ingrese la carrera del estudiante: ")
    varEstudiante.append(varCarrera)
    varPromedio = int(input("Ingrese el promedio del estudiante: "))
    # Comprobar que el promedio academico este dentro del rango 0-100
    if varPromedio < 0 or varPromedio > 100:
        print("Promedio invalido. Ingrese un promedio entre 0-100")
        return
    varEstudiante.append(varPromedio)

    # Almacenar los datos dentro de la lista principal
    varListaEstudiante.append(varEstudiante)
    print("***Estudiante registrado correctamente***")
    VolverMenu()


def MostrarEstudiantes():
    print("Lita de estudiantes ordenados por nombre, codigo, edad, carrera y promedio \n")
    print(varListaEstudiante)
    VolverMenu()


login()
menu()
