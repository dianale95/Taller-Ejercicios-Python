import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_profesion, deco_rot13

# Ejercicio 24:
# ¿Cuántos registros tienen nombre "Ana" y son "Medico"?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: deco_rot13(x))
df_nombre_profesion = limpiar_profesion(df)

# Filtro y conteo
nombre = "Ana"
profesion = "Medico"

resultado_filtro = (df_nombre_profesion['nombre_cifrado'].str.lower() == nombre.lower()) & (df_nombre_profesion['profesion'].str.lower() == profesion.lower())

count_filtro = len(df_nombre_profesion[resultado_filtro])

print(f"El total de registros con nombre 'Ana' y profesion 'Medico' es {count_filtro}")