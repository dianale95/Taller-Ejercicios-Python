#Cargar datos
import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')
#----------------------------------------
#--------Fin cargar datos----------------

texto_original = "Juan"

#Cifrar ROT13
texto_cifrado = codecs.encode(texto_original,'rot_13')

condicion = datos['nombre_cifrado'] == texto_cifrado

datos_nuevos =datos[condicion]

print(datos_nuevos.shape[0])
print(datos_nuevos)