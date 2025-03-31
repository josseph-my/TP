
# lista principal de estudiantes
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

# mostrar estudiantes


varEstudiante = []


def MostrarEstudiantes():
    for est in varEstudiantes:
        print("\n", varEstudiante, "\n")


RegistrarEstudiante()

MostrarEstudiantes()
