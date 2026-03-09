import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv

# Ejercicio 01: 
# ¿Cuántas filas tienen el campo id con caracteres no numéricos?

df = cargar_csv("personas.csv")

# Conteo de campo id no numéricos
count_id_no_num = (~df["id"].str.isnumeric()).sum()

print(f"Hay {count_id_no_num} filas con id que contienen caracteres no numéricos")