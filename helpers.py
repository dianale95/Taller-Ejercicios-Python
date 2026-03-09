import pandas as pd
import codecs

# Función para cargar archivo csv y retorna como un DataFrame

def cargar_csv(archivo):
    df_datos = pd.read_csv("./data/"+archivo)
    return df_datos

# Función para decodificar texto ROT13

def deco_rot13(texto): 
    return codecs.decode(texto, "rot13")