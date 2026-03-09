import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, limpiar_email

# Ejercicio 29:
# ¿Cuántos registros tienen email con dominio "gmail.com"?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df_email = limpiar_email(df)

# Filtro y conteo
dominio = "gmail.com"

count_email = df_email['email'].str.endswith(f'@{dominio}', na=False).sum()

print(f"El total de registros con email de gmail es {count_email}")