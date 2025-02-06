"""La sentencia condicionalmultiple 
la sentencia condicional multiple se utiliza cuando hay varias condiciones 
en python, se usa if, elif, else"""

edad = int(input("Digite la edad "))
if edad >= 18:
    print("es mayor de edad ")
elif edad >= 13: # de lo contrario
    print("Es un adolecente")
else:
    print("Es un niño")

