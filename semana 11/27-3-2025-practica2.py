# programa que en una funcion que lea palabras y cuente las vocales e imprimirlass

def lector(palabra):

    consVocales = "aeiouAEIOU"
    varContador = 0

    for letra in palabra:
        if letra in consVocales:
            varContador += 1

    return varContador


varPalabra = input("Introduce la palabra: ")
varResultado = lector(varPalabra)
print(f"La palabra '{varPalabra}' tiene {varResultado} vocales")
