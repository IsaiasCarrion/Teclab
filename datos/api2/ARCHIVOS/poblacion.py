import pandas as pd
import numpy as np
import os
os.chdir("C:\\Users\\Izzy\\Documents\\GitHub\\Teclab\\datos\\api2\\ARCHIVOS\\")

# Importamos los archivos csv con los datos q vamos a utilizar
# Poblacion Anual
poblacion_anual = pd.read_csv("poblacion.csv", encoding="latin-1")

# Densidad Poblacional
densidad_poblacional = pd.read_csv("poblacion_con_densidad.csv", encoding="latin-1")

# Hogares viviendas x superficie
hongares_superficie = pd.read_csv("hogares_viviendas_superficie.csv", encoding="latin-1")

# Exploracion de Head
poblacion_anual.head()

# Exploracion del Tail
poblacion_anual.tail()

# Filas y Columnas
print("Las filas y columnas son: ")
poblacion_anual.shape
print(poblacion_anual)

# Tipos de datos
poblacion_anual.dtypes