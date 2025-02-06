# calcular el total a pagar por una compra

varCantidad = int(input("Ingrese la cantidad de productos "))
varPrecio = int(input("Ingrese el precio del producto en colones "))
varImpuesto = int(input("Ingrese el impuesto que se aplicará "))

varImpuesto = varImpuesto/100
varImpuesto = varPrecio * varImpuesto
varPrecioT = varPrecio + varImpuesto

print("El total a pagar seria de",varPrecioT,"colones")
