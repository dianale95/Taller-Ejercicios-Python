import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, deco_rot13

# Ejercicio 04: 
# ¿Cuál es el nombre más frecuente y cuántas veces aparece?

df = cargar_csv("personas.csv")

# Decodificar columna nombre_cifrado
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: deco_rot13(x)) 

# Frecuencia de cada nombre en nombre_cifrado
count_name = df["nombre_cifrado"].value_counts() 

# Nombre más frecuente en count_name
max_name = count_name.idxmax() 

# Total del conteo en count_name
total_name = count_name.max() 

print(f"El nombre más frecuente en el dataset es '{max_name}' y aparece {total_name} veces") 