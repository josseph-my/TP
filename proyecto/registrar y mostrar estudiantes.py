
# lista principal de estudiantes
varEstudiantes = []

# registrar estudiantes


def RegistrarEstudiante():

    varCodigo = int(input("Ingrese el codigo del estudiante: "))

# Comprobar que codigo no sea igual a otro ya registrado
    for est in varEstudiantes:
        if est[varCodigo] == varCodigo:
            print("Codigo ya registrado.")
            return
    varNombre = input("Ingrese el nombre del estudiante: ")
    varEdad = int(input("Ingrese la edad del estudiante: "))
    varCarrera = input("Ingrese la carrera del estudiante: ")
    varPromedio = float(input("Ingrese el promedio de estudiante: "))

# Comprobar que el promedio este en rango valido (0-100)
    if varPromedio < 0 or varPromedio > 100:
        print("Promedio invalido. Ingrese un promedio entre 0-100")
        return

    varEstudiantes.append({
        'codigo': varCodigo,
        'nombre': varNombre,
        'edad': varEdad,
        'carrera': varCarrera,
        'promedio': varPromedio
    })
    print("***Estudiante registrado correctamente***")
    print("\n" * 2)

# mostrar estudiantes


def MostrarEstudiantes():
    for est in varEstudiantes:
        print(
            f"Código: {est['codigo']}, Nombre: {est['nombre']}, Edad: {est['edad']},Carrera: {est['carrera']}, Promedio: {est['promedio']}")
        print("\n" * 2)


RegistrarEstudiante()

MostrarEstudiantes()
