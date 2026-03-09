import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv

# Ejercicio 19: 
# ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD?

df = cargar_csv("personas.csv")

# Conteo de registros que NO tienen formato YYYY-MM-DD
fecha_valida = df['fecha_nacimiento'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False).sum()
fecha_otros = len(df) - fecha_valida

print(f"El total de registros de fecha de nacimiento con formato diferente a YYYY-MM-DD es {fecha_otros}")