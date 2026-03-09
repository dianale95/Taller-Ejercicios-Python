import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_salario

# Ejercicio 15: 
# ¿Cuál es el salario máximo después de limpiar?

df = cargar_csv("personas.csv")

# DataFrame con columna salario limpia
df_salario = limpiar_salario(df)

salario_max = df_salario["salario"].max()
print(f"El salario máximo después de limpiar es {salario_max:,.2f}")

