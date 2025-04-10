# from Persona import Persona


# persona1 = Persona("Brandom", 23)
# persona1.saludar()

# Mostrar los multiplos de 3 entre 1 y 100 usando for
for num in range(1, 101):
    if num % 3 == 0:
        print(num)


# Pedir numeros hasta que el usuario ingrese cero y mostrarel total ingresado
varSuma = 0
while True:
    varNum = int(input("Ingrese un numero: "))
    varSuma += varNum
    if varNum == 0:
        break

print(f"La suma de los numeros es {varSuma}")


# Calcular la suma de los digitos de un numero entero
varEntero = input("Ingrese el numero entero positivo: ")
varSuma = 0
for i in varEntero:
    if i.isdigit():
        varSuma += int(i)

print(f"La suma de los digitos es {varSuma}")


# Mostrar cuenta regresiva de 10 a 1 con while
varCuenta = 10
while True:
    print(varCuenta)
    varCuenta -= 1
    if varCuenta == 0:
        break


# Crear una clase animal con atributo especie y mostrar la especie de 5 animales
# ingresados por el usuario
class AnimalC:
    varAnimal = ""
    varEspecie = ""

    def __init__(self, pAnimal, pEspecie):
        self.varAnimal = pAnimal
        self.varEspecie = pEspecie

    def MostrarEspecie(self):
        print(f"El animal {self.varAnimal} es de la especie {self.varEspecie}")


animales = []
for i in range(5):
    varAnimales = input("Ingrese el animal: ")
    animales.append(varAnimales)

especies = []
for i in range(5):
    varEspecies = input("Ingrese la especie: ")
    especies.append(varEspecies)

for animal, especie in zip(animales, especies):
    p = AnimalC(animal, especie)
    p. MostrarEspecie()

# Leer 5 edades con un bucle y mostrar cuantas son mayores de edad
c = 0
for i in range(5):
    varEdad = int(input(f"Ingrese la edad {i + 1}: "))
    if varEdad >= 18:
        c += 1

print(f"Hay {c} mayores de edad")

# crear una clase libro con titulo y autor. leer 3 libros desde el teclado y mostrarlos


class Libro:
    varLibros = ""
    varAutores = ""

    def __init__(self, pLibro, pEdad):
        self.varLibros = pLibro
        self.varAutores = pEdad

    def mostrar(self):
        print(f"El libro {self.varLibros} es del autor {self.varAutores} ")


varTitulos = []
for i in range(3):
    varLibro = input(f"Ingrese el titulo del libro {i + 1}: ")
    varTitulos.append(varLibro)

for libro in (varTitulos):
    p = Libro(libro, "cervantes")
    p.mostrar()


# Escribir un programa que use for y continue para mostrar los numeros
# del 1 al 10, excepto el 5
for i in range(11):
    if i == 5:
        continue
    print(i)
