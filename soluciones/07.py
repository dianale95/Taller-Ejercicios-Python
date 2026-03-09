import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_ciudad

# Ejercicio 07: 
# ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar?

df = cargar_csv("personas.csv")

# DataFrame con columna ciudad limpia
df_ciudad = limpiar_ciudad(df)

# Conteo de registros con ciudad "Bogota"
ciudad = 'medellin'
conteo_ciudad = df_ciudad[df_ciudad["ciudad"] == ciudad.lower()].shape[0]

print(f"El total de registros con ciudad '{ciudad}' es {conteo_ciudad}")