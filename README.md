# Taller de Python - Manejo y Limpieza de Datos

## Infraestructura para Grandes Volúmenes de Datos

---

## Estructura del Repositorio

El repositorio debe contener:

```
├── soluciones/
│   ├── 01.py
│   ├── 02.py
│   ├── 03.py
│   ├── ...
│   └── 30.py
├── data/
│   └── personas.csv
├── helpers.py
└── README.md  (con las soluciones)
```

Cada archivo `.py` dentro de la carpeta `soluciones/` debe contener el código que resuelve el ejercicio correspondiente.

Helpers.py es un archivo que sirve para reutilizar funciones en todos los ejercicios

---

## Sobre el Dataset

- **Archivo:** `data/personas.csv`
- **Registros:** 300,000 filas
- **Columnas:** `id`, `nombre_cifrado`, `apellido_cifrado`, `ciudad`, `profesion`, `email`, `fecha_nacimiento`, `salario`, `activo`

### Datos sucios

El dataset tiene intencionalmente datos sucios en el 30% de cada columna:
- Espacios adicionales
- Caracteres especiales (@, %, #)
- Mayúsculas inconsistentes
- Formatos variados

### Descifrar nombres y apellidos

Los campos `nombre_cifrado` y `apellido_cifrado` usan cifrado ROT13:

```python
import codecs
nombre = codecs.decode(texto, 'rot_13')
```

---

## Ejercicios y Soluciones

A continuación se listan los 30 ejercicios. **Debe escribir el valor exacto de la respuesta** en la columna "Solución".

| # | Ejercicio | Solución |
|---|-----------|----------|
| 01 | ¿Cuántas filas tienen el campo `id` con caracteres no numéricos? | `83648` |
| 02 | ¿Cuántas veces aparece el nombre "Maria" en el dataset? | `4160` |
| 03 | ¿Cuántas veces aparece el nombre "Juan" en el dataset? | `3986` |
| 04 | ¿Cuál es el nombre más frecuente y cuántas veces aparece? | `GONZALO, 4221` |
| 05 | ¿Cuál es el apellido más frecuente y cuántas veces aparece? | `REYES, 7490` |
| 06 | ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar? | `14969` |
| 07 | ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar? | `15193` |
| 08 | ¿Cuántas ciudades únicas existen después de normalizar? | `25` |
| 09 | ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar? | `12083` |
| 10 | ¿Cuántos registros tienen la profesión "Programador" después de limpiar? | `12062` |
| 11 | ¿Cuántas profesiones únicas existen después de normalizar? | `25` |
| 12 | ¿Cuántos registros tienen el campo `email` con espacios adicionales? | `45447` |
| 13 | ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos? | `85266` |
| 14 | ¿Cuál es el salario promedio después de limpiar? | `8,005,689.17` |
| 15 | ¿Cuál es el salario máximo después de limpiar? | `14,999,995.00` |
| 16 | ¿Cuál es el salario mínimo después de limpiar? | `1,000,032.00` |
| 17 | ¿Cuántos registros tienen `activo` como verdadero después de normalizar? | `149863` |
| 18 | ¿Cuántos registros tienen `activo` como falso después de normalizar? | `150137` |
| 19 | ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD? | `89823` |
| 20 | ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? | `53404` |
| 21 | ¿Cuántas personas nacieron antes de 1960? | `66577` |
| 22 | ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)? | `139961` |
| 23 | ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"? | `187` |
| 24 | ¿Cuántos registros tienen nombre "Ana" y son "Medico"? | `172` |
| 25 | ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000? | `4405` |
| 26 | ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980? | `3241` |
| 27 | ¿Cuál es la ciudad con más "Ingenieros"? | `popayan con 640 ingenieros` |
| 28 | ¿Cuál es la profesión con el salario promedio más alto? | `biologo con 8,073,516.86` |
| 29 | ¿Cuántos registros tienen email con dominio "gmail.com"? | `60000` |
| 30 | ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? | `96` |

---

## Ejemplo de Solución

### Archivo `soluciones/02.py`

```python
import pandas as pd
import codecs

# Cargar datos
df = pd.read_csv('data/personas.csv')

# Descifrar nombres con ROT13
df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Contar cuántas veces aparece "Maria"
cantidad = df[df['nombre'] == 'Maria'].shape[0]

print(f"El nombre 'Maria' aparece {cantidad} veces")
```

### En el README, la solución se vería así:

| # | Ejercicio | Solución |
|---|-----------|----------|
| 02 | ¿Cuántas veces aparece el nombre "Maria" en el dataset? | `15234` |

*(El número 15234 es solo un ejemplo, debe calcular el valor real)*

---

## Comandos Útiles

```bash
# Ejecutar un script de solución
uv run python soluciones/01.py

# O si no usa uv
python soluciones/01.py
```

---

## Dependencias

El proyecto usa `pandas` y `matplotlib`. Si usa `uv`:

```bash
uv add pandas matplotlib
```

Si usa `pip`:

```bash
pip install pandas matplotlib
```
