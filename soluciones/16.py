import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_salario

# Ejercicio 16: 
# ¿Cuál es el salario mínimo después de limpiar?

df = cargar_csv("personas.csv")

# DataFrame con columna salario limpia
df_salario = limpiar_salario(df)

salario_min = df_salario["salario"].min()
print(f"El salario máximo después de limpiar es {salario_min:,.2f}")

