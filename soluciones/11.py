import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_profesion

# Ejercicio 11: 
# ¿Cuántas profesiones únicas existen después de normalizar?

df = cargar_csv("personas.csv")

# DataFrame con columna profesión limpia
df_profesion = limpiar_profesion(df)

# Conteo profesiones únicas después de limpiar
total_profesiones = df_profesion["profesion"].nunique()  
print(f"El total de profesiones únicas es: {total_profesiones}")