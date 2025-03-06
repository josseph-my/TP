# programa que solicite al usuario dos numeros y muestre su suma
# resta, multiplicacion y division.

varNum1 = float(input("Ingrese el primer numero:"))
varNum2 = float(input("Ingrese el segundo numero:"))

varSuma = varNum1 + varNum2
varResta = varNum1 - varNum2
varMult = varNum1 * varNum2
varDivi = varNum1 / varNum2

print("El resultado de la suma es ", varSuma, " el de la resta es ", varResta,
      "el de la multiplicacion es ", varMult, "y el de la division es ", varDivi)
