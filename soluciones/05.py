import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, deco_rot13

# Ejercicio 05: 
# ¿Cuál es el apellido más frecuente y cuántas veces aparece?

df = cargar_csv("personas.csv")

# Decodificar columna apellido_cifrado
df["apellido_cifrado"] = df["apellido_cifrado"].apply(lambda x: deco_rot13(x)) 

# Frecuencia de cada apellido en apellido_cifrado
count_lastname = df["apellido_cifrado"].value_counts() 

# Apellido más frecuente en count_lastname
max_lastname = count_lastname.idxmax() 

# Total del conteo en count_lastname
total_lastname = count_lastname.max() 

print(f"El apellido más frecuente en el dataset es '{max_lastname}' y aparece {total_lastname} veces") 