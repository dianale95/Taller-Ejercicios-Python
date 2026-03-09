import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_salario

# Ejercicio 14: 
# ¿Cuál es el salario promedio después de limpiar?

df = cargar_csv("personas.csv")

# DataFrame con columna salario limpia
df_salario = limpiar_salario(df)

promedio_salario = df_salario["salario"].mean()
print(f"El salario promedio después de limpiar es {promedio_salario:,.2f}")

