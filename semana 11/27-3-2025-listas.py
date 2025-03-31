
nombres = ["Vale", "Juan", "Mont"]
nombres.append("Jon")
nombres.append("Brandom")

print(nombres[1])

nombres.remove("Jon")

print(nombres)


print(nombres[3].upper())
print(nombres[3].lower())
print(nombres[3].replace("a", "@"))

animales = ["oso", "perro", "gato", "iguana"]

for animal in animales:
    if animal[0].lower() in "aeiou":
        print(animal)

frase = "programar en python es divertido"
contador = frase.count("a")
print("La letra 'a' aparece", contador, "veces.")

texto = nombres(0)
for letras in texto:
    print(letras)
