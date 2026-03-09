import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv

# Ejercicio 13: 
# ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos?

df = cargar_csv("personas.csv")

count_no_numerics = df["salario"].str.contains("[^0-9]").sum()
print("El total de registros con caracteres no numéricos en el campo salario es ", count_no_numerics)