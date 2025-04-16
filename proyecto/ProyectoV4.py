# Variables de listas globales de estudiantes
varNombresLista = []
varNotasLista = []
varPromediosLista = []


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
    varOpcion = input("\nSeleccione el número de opción: ")

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
    varVolver = input("\n¿Desea volver al menu? si/no ")
    if varVolver.lower() == "si":
        menu()
    else:
        print("Ha salido del menu ")


# Funcion de regsitro de estudiantes y guardarlas en la variable global de nombres
def RegistrarEstudiante():
    varNombre = input("\nIngrese el nombre del estudiante a registrar: ")
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
    print("\n**Notas registradas correctamente**")
    VolverMenu()


# Funcion para mostrar datos de estudiantes (nombres y notas)
def MostrarDatos():
    print("\n**Lista de notas**")
    for nombre, nota in zip(varNombresLista, varNotasLista):
        print(
            f"Las notas del estudiante: {nombre} son: {nota}")
    VolverMenu()


# Se calcula el promedio de cada estudiante
def CalcularPromedio():
    print("\n**Promedios de notas**")
    for varNombre, varNota in zip(varNombresLista, varNotasLista):
        varPromedio = sum(varNota)/len(varNota)
        varPromediosLista.append(varPromedio)
        print(f"{varNombre} tiene un promedio de {varPromedio}")
    VolverMenu()


# Se clasifica el promedio de los estudiantes
def ClasificarRendimiento():
    print("\n**Clasificacion de rendimiento**")
    for varNombre, varPromedio in zip(varNombresLista, varPromediosLista):
        if varPromedio >= 0 and varPromedio < 60:
            print(f"El rendimiento de {varNombre} es insuficiente o bajo")
        elif varPromedio >= 60 and varPromedio <= 69:
            print(F"El rendimiento de {varNombre} es regular")
        elif varPromedio >= 70 and varPromedio <= 79:
            print(f"El rendimiento de {varNombre} es bueno")
        elif varPromedio >= 80 and varPromedio <= 89:
            print(f"El rendimiento de {varNombre} es muy bueno")
        elif varPromedio >= 90 and varPromedio <= 100:
            print(f"El rendimiento de {varNombre} es excelente")
    VolverMenu()


login()
menu()
