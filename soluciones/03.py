import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, deco_rot13

# Ejercicio 02: 
# ¿Cuántas veces aparece el nombre "Maria" en el dataset?

df = cargar_csv("personas.csv")

# Decodificar columna nombre_cifrado
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: deco_rot13(x)) 

# Nombre a buscar
name = "Juan" 

# Conteo de campo nombre_cifrado igual a name
count_name = (df["nombre_cifrado"]==name).sum() 

print(f"El nombre '{name}' aparece {count_name} veces en el dataset")