import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_ciudad

# Ejercicio 08: 
# ¿Cuántas ciudades únicas existen después de normalizar?

df = cargar_csv("personas.csv")

# DataFrame con columna ciudad limpia
df_ciudad = limpiar_ciudad(df)

# Conteo ciudades únicas después de limpiar
total_ciudades = df_ciudad["ciudad"].nunique()  
print(f"El total de ciudades únicas es: {total_ciudades}")

