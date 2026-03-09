import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_profesion, limpiar_salario

# Ejercicio 25:
# ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df_profesion = limpiar_profesion(df)
df_profesion_salario = limpiar_salario(df_profesion)

# Filtro y conteo
profesion = "Abogado"
salario = 10000000

resultado_filtro = (df_profesion_salario['profesion'].str.lower() == profesion.lower()) & (df_profesion_salario['salario'] > salario)

count_filtro = len(df_profesion_salario[resultado_filtro])

print(f"El total de registros con profesión 'Abogado' y salario > 10,000,000 es {count_filtro}")