
varP = int(input("Cuantos payasos se enviaron en el paquete "))
varM = int(input("Cuantas muñecas se emviaron en el paquete "))

varPesoP = 112
varPesoM = 75

varPTP = varPesoP * varP  # peso total payasos
varPTM = varPesoM * varM  # peso total muñecas

varTotal = varPTM + varPTP

print("El total de peso de todos los articulos es de ", varTotal)
