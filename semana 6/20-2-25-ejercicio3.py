
cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual (en porcentaje): "))
años = int(input("Ingrese el numero de años: "))

contador = 1
interes_generado = cantidad * interes_anual / 100
capital = 0

while contador <= años:
    capital += interes_generado
    contador += 1

print("El capital total invertido de la inversion es", capital)
