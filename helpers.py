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