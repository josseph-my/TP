
varBollos = int(input("cuantos bolllos que no son del dia se vendieron "))

consBollos = 700

varT = consBollos * varBollos

varD = varT / 100 * 60

varTD = varT - varD

print("El precio habitual es de", varT, ", el descuento es de",
      varD, "y el precio final es", varTD)
