import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_fecha_nacimiento

# Ejercicio 21: 
# ¿Cuántas personas nacieron antes de 1960?

df = cargar_csv("personas.csv")

# DataFrame con columna fecha_nacimiento limpia
df_fecha_nacimiento = limpiar_fecha_nacimiento(df)

limite = 1960

# Conteo de registros con fecha_nacimiento menor al limite
count_fecha = (df_fecha_nacimiento['fecha_nacimiento'].dt.year < limite).sum()

print(f"El total de personas nacidas antes de {limite} es {count_fecha}")