import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_fecha_nacimiento

# Ejercicio 20: 
# ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)?

df = cargar_csv("personas.csv")

# DataFrame con columna fecha_nacimiento limpia
df_fecha_nacimiento = limpiar_fecha_nacimiento(df)

limite_inf, limite_sup = 1990, 2000

# Conteo de registros con fecha_nacimiento entre el rango
count_fecha = df_fecha_nacimiento['fecha_nacimiento'].dt.year.between(limite_inf, limite_sup).sum()

print(f"El total de personas nacidas entre {limite_inf} y {limite_sup} es {count_fecha}")