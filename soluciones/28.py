import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_profesion, limpiar_salario

# Ejercicio 28:
# ¿Cuál es la profesión con el salario promedio más alto?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df_profesion = limpiar_profesion(df)
df_profesion_salario = limpiar_salario(df_profesion)

# Resultado
conteo_profesion = df_profesion_salario.groupby('profesion')['salario'].mean()
profesion_top = conteo_profesion.idxmax()
salario_promedio = conteo_profesion.max()
print(f"La profesión con el salario promedio más alto es {profesion_top} con {salario_promedio:,.2f}")