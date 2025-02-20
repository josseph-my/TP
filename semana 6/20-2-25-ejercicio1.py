
varPeso = input("Cual es tu peso en kg? ")
varEstatura = input("Cual es tu estatura en metros ")
imc = round(float(varPeso) / float(varEstatura) ** 2, 4)

print("Tu indice de masa corporal es " + str(imc))
