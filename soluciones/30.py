import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helpers import cargar_csv, deco_rot13

# Ejercicio 29:
# ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"?

df = cargar_csv("personas.csv")

# Limpieza de columnas
df['nombre_cifrado'] = df['nombre_cifrado'].apply(lambda x: deco_rot13(x))
df_clean = df.copy()
df_clean['apellido_cifrado'] = df_clean['apellido_cifrado'].apply(lambda x: deco_rot13(x))

# Filtro y conteo
nombre = "Jose"
apellido = "Garcia"
mask = (df_clean['nombre_cifrado'].str.lower() == nombre.lower()) & \
       (df_clean['apellido_cifrado'].str.lower() == apellido.lower())
cantidad = len(df_clean[mask])
print(f"El total de registros con nombre 'Jose' y apellido 'Garcia' es {cantidad}")