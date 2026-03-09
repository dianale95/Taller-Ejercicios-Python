import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_ciudad, deco_rot13

# Ejercicio 23:
# ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: deco_rot13(x)) 
df_nombre_ciudad = limpiar_ciudad(df)

# Filtro y conteo
nombre = "Carlos"
ciudad = "Cali"

resultado_filtro = (df_nombre_ciudad['nombre_cifrado'].str.lower() == nombre.lower()) & (df_nombre_ciudad['ciudad'].str.lower() == ciudad.lower())

count_filtro = len(df_nombre_ciudad[resultado_filtro])

print(f"El total de registros con nombre 'Carlos' y ciudad 'Cali' es {count_filtro}")