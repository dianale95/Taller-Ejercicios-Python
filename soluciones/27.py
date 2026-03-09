import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_ciudad, limpiar_profesion

# Ejercicio 27:
# ¿Cuál es la ciudad con más "Ingenieros"?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df_ciudad = limpiar_ciudad(df)
df_ciudad_profesion = limpiar_profesion(df_ciudad)

# Filtro y resultado
profesion = "Ingeniero"

conteo_ciudad = df_ciudad_profesion[df_ciudad_profesion['profesion'].str.lower() == profesion.lower()].groupby('ciudad')['profesion'].count()

ciudad_top = conteo_ciudad.idxmax()

total = conteo_ciudad.max()

print(f"La ciudad con más ingenieros es {ciudad_top} con {total} ingenieros")