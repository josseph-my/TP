

# Variable global de estudiantes
varNombresLista = []
varNotasLista = []

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
    print("\n**Menu de opciones**")
    print("1-Registrar estudiante")
    print("2-Agregar notas")
    print("3-Mostrar datos")
    print("4-Calcular promedio")
    print("5-Clasificar rendimiento")
    print("6-Salir")

    # Selección y funciones según la opción escogida
    varOpcion = input("Seleccione el número de opción: ")

    if varOpcion == "1":
        RegistrarEstudiante()
    elif varOpcion == "2":
        AgregarNotas()
    elif varOpcion == "3":
        MostrarDatos()
    elif varOpcion == "4":
        CalcularPromedio()
    elif varOpcion == "5":
        ClasificarRendimiento()
    elif varOpcion == "6":
        print("Ha salido del menu")
    else:
        print("Opción inválida. Intente nuevamente.")
        menu()

# Funcion para volver o salir


def VolverMenu():
    varVolver = input("Desea volver al menu ")
    if varVolver.lower() == "si":
        menu()
    else:
        print("Ha salido del menu ")

# Funcion de regsitro de estudiantes y guardarlas en la variable global de nombres


def RegistrarEstudiante():
    varNombre = input("Ingrese el nombre del estudiante a registrar: ")
    varNombresLista.append(varNombre)
    print("\n*Estudiante registrado correctamente*")
    VolverMenu()


# Funcion para agregar notas y guardarlas en la variable global de notas


def AgregarNotas():
    varNotas = []
    print("\n**Ingrese las notas requeridas**")
    for i in range(4):
        varNotaInd = int(input(f"Nota del curso {i + 1}: "))
        varNotas.append(varNotaInd)

    varNotasLista.append(varNotas)
    print("\n*Notas registradas correctamente*")
    VolverMenu()


# Funcion para mostrar datos


def MostrarDatos():
    for nombre, nota in zip(varNombresLista, varNotasLista):
        print(
            f"Las notas del estudiante: {nombre} son: {nota}")
    VolverMenu()


menu()
