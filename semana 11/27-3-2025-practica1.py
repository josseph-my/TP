
varEsts = int(input("Cuantos estudiantes desea matricular: "))
i = 0
varListaEst = []
while i < varEsts:
    varNombre = input("Ingrese el nombre del estudiante: ")

    varListaEst.append(varNombre)
    i += 1

print(varListaEst)
