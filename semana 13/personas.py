
class Estudiante:
    varMedia = 0

    def __init__(self, pNotas):
        self.varNotas = pNotas

    def media(self):
        print(f"La media es{self.media}")


varTotal = 0
for i in range(3):
    num = float(input(f"Ingrese la nota {i + 1}:"))
    varTotal += num

varTotal/3

for nota in range(3):
    p = Estudiante(nota)
    p.media()
