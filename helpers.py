import pandas as pd

# Función para cargar archivo csv y retorna como un DataFrame

def cargar_csv(archivo):
    df_datos = pd.read_csv("./data/"+archivo)
    return df_datos