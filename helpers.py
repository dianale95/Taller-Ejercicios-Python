import pandas as pd
import codecs
import numpy as np
import re
import unicodedata
from thefuzz import process, fuzz

# Función para cargar archivo csv y retorna como un DataFrame

def cargar_csv(csv):
    df_datos = pd.read_csv("./data/"+csv)
    return df_datos

# Función para decodificar texto ROT13

def deco_rot13(texto): 
    return codecs.decode(texto, "rot13")

# Normaliza y corrige valores mal escritos en la columna ciudad
def limpiar_ciudad(df, col='ciudad', umbral=80, min_frecuencia=1000):
    def limpiar(texto):
        if isinstance(texto, str):
            texto = texto.strip()
            texto = texto.lower()
            texto = unicodedata.normalize('NFD', texto)
            texto = texto.encode('ascii', 'ignore').decode('utf-8')
            texto = ''.join([c for c in texto if not c.isdigit()])
            texto = re.sub(r'[^a-zA-Z\s]', '', texto)
        return texto

    df[col] = df[col].apply(limpiar)

    conteo = df[col].value_counts()
    texto_valido = conteo[conteo > min_frecuencia].index.tolist()

    def corregir(texto):
        texto = str(texto).strip().lower()
        if texto in texto_valido:
            return texto
        resultado = process.extractOne(texto, texto_valido, scorer=fuzz.token_set_ratio)
        if resultado and resultado[1] >= umbral:
            return resultado[0]
        return texto

    df[col] = df[col].apply(corregir)
    return df

# Normaliza y corrige valores mal escritos en la columna profesion
def limpiar_profesion(df, col='profesion', umbral=80, min_frecuencia=1000):
    def limpiar(texto):
        if isinstance(texto, str):
            texto = texto.strip()
            texto = texto.lower()
            texto = unicodedata.normalize('NFD', texto)
            texto = texto.encode('ascii', 'ignore').decode('utf-8')
            texto = ''.join([c for c in texto if not c.isdigit()])
            texto = re.sub(r'[^a-zA-Z\s]', '', texto)
        return texto

    df[col] = df[col].apply(limpiar)

    conteo = df[col].value_counts()
    texto_valido = conteo[conteo > min_frecuencia].index.tolist()

    def corregir(texto):
        texto = str(texto).strip().lower()
        if texto in texto_valido:
            return texto
        resultado = process.extractOne(texto, texto_valido, scorer=fuzz.token_set_ratio)
        if resultado and resultado[1] >= umbral:
            return resultado[0]
        return texto

    df[col] = df[col].apply(corregir)
    return df

# Normaliza y limpia valores numéricos de moneda en la columna salario
def limpiar_salario(df, col='salario'):
    def limpiar_valor(valor):
        if pd.isna(valor):
            return np.nan
        valor_str = str(valor).strip().lower()
        # Texto seguido de punto y número. Ejemplo: aprox.10001178
        match = re.search(r'[a-z]+\.(\d+)', valor_str)
        if match:
            return match.group(1)
        # Reemplazamos letras similares a números
        valor_str = valor_str.replace('l', '1').replace('o', '0')
        # Eliminamos símbolos al inicio y al final
        valor_str = re.sub(r'^[^0-9]+|[^0-9]+$', '', valor_str)
        if not valor_str:
            return np.nan
        # Puntos de miles y coma decimal. Ejemplo: 1.250,50
        if '.' in valor_str and ',' in valor_str:
            valor_str = valor_str.replace('.', '')
            valor_str = valor_str.replace(',', '.')
        # Solo coma decimal. Ejemplo: 1250,50
        elif ',' in valor_str:
            valor_str = valor_str.replace(',', '.')
        # Quitamos todo excepto números y punto decimal
        valor_limpio = re.sub(r'[^0-9.]', '', valor_str)
        # Si quedaron múltiples puntos dejamos solo el último
        if valor_limpio.count('.') > 1:
            partes = valor_limpio.split('.')
            valor_limpio = "".join(partes[:-1]) + "." + partes[-1]
        if not valor_limpio or valor_limpio == '.':
            return np.nan
        return valor_limpio

    df[col] = df[col].apply(limpiar_valor)
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df.loc[df[col] < 0, col] = np.nan
    return df