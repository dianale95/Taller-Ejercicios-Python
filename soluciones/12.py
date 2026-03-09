import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv

# Ejercicio 12: 
# ¿Cuántos registros tienen el campo `email` con espacios adicionales?

df = cargar_csv("personas.csv")

count_espacios = df["email"].str.contains(" ").sum()
print("El total de registros con espacios adicionales en el campo email es ", count_espacios)