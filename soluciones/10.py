import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_profesion

# Ejercicio 10: 
# ¿Cuántos registros tienen la profesión "Programador" después de limpiar?

df = cargar_csv("personas.csv")

# DataFrame con columna ciudad limpia
df_profesion = limpiar_profesion(df)

# Conteo de registros con profesión "Programador"
profesion = 'Programador'
conteo_profesion = df_profesion[df_profesion["profesion"] == profesion.lower()].shape[0]

print(f"El total de registros con profesión '{profesion}' es {conteo_profesion}")