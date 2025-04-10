

class Persona:
    # Constructor por parametros
    varNombre = ""
    varEdad = 0

    def __init__(self, Pnombre, Pedad):
        self.varNombre = Pnombre
        self.varEdad = Pedad

    def saludar(self):
        print(f" Hola me llamo {self.varNombre}y tengo {self.varEdad}años")
