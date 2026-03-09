import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_fecha_nacimiento, calcular_edad

# Ejercicio 22: 
# ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)?

df = cargar_csv("personas.csv")

# DataFrame con columna fecha_nacimiento limpia
df_fecha_nacimiento = limpiar_fecha_nacimiento(df)

# Agregar columna edad
df_fecha_nacimiento['edad'] = df_fecha_nacimiento['fecha_nacimiento'].apply(calcular_edad)

# Conteo de registros con edad mayor a 50
count_mayores = (df_fecha_nacimiento['edad'] > 50).sum()

print(f"El total de personas con más de 50 años es {count_mayores}")