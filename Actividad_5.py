#Este es el script para la actividad 5

# Importo las bibliotecas necesarias.
import pandas as pd

# Leo los datos del archivo csv que está en linea
data = pd.read_csv('https://raw.githubusercontent.com/cat-coding-cat/SimpleDataSets/main/Museos_vs_EdadVisitantes.csv')

# Imprimo los datos para ver si todo está bien
print(data)

edadDeLosVisitantes = data["EdadVisitantes"]

#Hago un print de la Variable
print("Print de la edad de los visitantes:")
print(edadDeLosVisitantes)

# para cada visitante imprimo su edad.
# si la edad es mayor de 40 imprime "You rock!"

for edad in edadDeLosVisitantes:
    if edad > 40:
        print("Edad : ", edad)
        print("You rock!")

print("Programa terminado")



# 1. Modifica el script anterior para indicar si el visitante tiene menos de 21 años.

# 2. Modifica el programa anterior para encontrar franja de edad entre 17 y 25 años.
