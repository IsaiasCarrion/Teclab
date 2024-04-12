# Importamos la librerias Pandas y Numpy
import pandas as pd
import numpy as np
import os
os.chdir("D:\Teclab Data\Practica")

#Importamos los archivos csv originales con los datos que vamos a usar:
#Datos macroeconomicos (PBI, Inflacion, Deuda, Resultado comercial y fiscal)
macro = pd.read("datos_macro.csv")

#Tipos de cambio de Brasil y de Argentina (precio del dolar en Reales y pesos Argentinos)
tc_br = pd.read_csv("tc_brasil.csv")
tc_ar = pd.read_csv("tc_argentina.csv")

#Exploramos las primeras filas del archivo de datos macroeconomicos
macro.head()

#Exploramos las ultimas filas del dataframe importado
macro.tail()

#Usamos shape para ver cuantas filas y columnas tiene y print para agregarle el texto
print("Las filas y las columnas son: ")
macro.shape

#chequeamos los tipos de variables que asigno al importar el dataframe
macro.dtypes

