import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_activo

# Ejercicio 17: 
# ¿Cuántos registros tienen `activo` como verdadero después de normalizar?

df = cargar_csv("personas.csv")

# DataFrame con columna activo limpia
df_activo = limpiar_activo(df)

# Conteo de registros con activo en verdadero
count_activo = df_activo[df_activo["activo"] == True].shape[0]

print(f"El total de registros con activo como verdadero es {count_activo}")