import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_ciudad, limpiar_activo, limpiar_fecha_nacimiento

# Ejercicio 26:
# ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df_ciudad = limpiar_ciudad(df)
df_ciudad_activo = limpiar_activo(df_ciudad)
df_clean = limpiar_fecha_nacimiento(df_ciudad_activo)

# Filtro y conteo
ciudad = "Barranquilla"
anio = 1980

resultado_filtro = (df_clean['ciudad'].str.lower() == ciudad.lower()) & (df_clean['activo'] == True) & (df_clean['fecha_nacimiento'].dt.year > anio)

count_filtro = len(df_clean[resultado_filtro])

print(f"El total de registros con ciudad 'Barranquilla', activos y nacidos después de 1980 ess {count_filtro}")