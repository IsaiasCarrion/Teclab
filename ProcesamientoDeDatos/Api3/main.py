"""
1 - Generar con pandas una serie de marcas de autos (Marcas_Autos), por
ejemplo "RENAULT","BMW", "TOYOTA", "FORD","CITROEN", "FIAT",
y compartir el output en una captura de pantalla donde se demuestre el
orden de las marcas de manera alfabética
"""

import pandas as pd
import numpy as np

marcas_autos = ["RENAULT", "BMW", "TOYOTA", "FORD", "CITROEN", "FIAT"]

serie_marcas = pd.Series(marcas_autos)
print(serie_marcas)

serie_marcas_ordenada = serie_marcas.sort_values(ascending=True)
print(serie_marcas_ordenada, "\n")


"""
2 - Usando pandas, vamos a crear un DataFrame que contenga: usuarios,
fecha, cantidad de consultas. Compartir el output en una captura de pantalla
donde se demuestre el DataFrame con sus datos requeridos.
Ejemplo de fecha: '2023-01-23'.
Ejemplo de usuario: 'gcastillo'.
Ejemplo de consulta: 7.
"""

usuarios = ['gcastillo', 'lmora', 'acuna', 'jmendez', 'ccruz']
fechas = ['2023-01-23', '2023-02-14', '2023-03-05', '2023-04-27', '2023-05-19']
consultas = [7, 15, 3, 11, 8]

df_usuarios = pd.DataFrame({
    'Usuarios': usuarios,
    'Fechas': pd.to_datetime(fechas),
    'Consultas': consultas
})

print(df_usuarios, "\n")


"""
3 – El objetivo general es crear una tabla dinámica usando pandas a través
de un DataFrame. En este ejercicio debemos compartir el output en una
captura de pantalla en 2 pasos. En el primer paso, mostrar el DataFrame con
sus datos requeridos, llamado (planilla_enero) que contenga los siguientes
datos aleatorios: "Nombre", "Fecha", "Consumos Mensuales".
"""

np.random.seed(10)  # Fijar semilla para resultados reproducibles

nombres = ['Ana', 'Luis', 'Carlos', 'María', 'Pedro']
fechas = pd.to_datetime(['2024-01-10', '2024-01-15', '2024-01-22', '2024-01-27', '2024-01-31'])
consumos_mensuales = np.random.randint(100, 500, size=5)

planilla_enero = pd.DataFrame({
    'Nombre': nombres,
    'Fecha': fechas,
    'Consumos Mensuales': consumos_mensuales
})

print(planilla_enero)
