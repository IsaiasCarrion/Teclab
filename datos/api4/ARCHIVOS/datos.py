import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir("D:/Teclab/datos/api4/ARCHIVOS/")
# Cargar los datos desde el archivo CSV
data = pd.read_csv("poblacion.csv")

# Visualización 1: Distribución de una variable (Histograma)
plt.figure(figsize=(8, 6))
sns.histplot(data['poblacion_total'], kde=True, color='skyblue')
plt.title('Distribución de la Población Total por Provincia')
plt.xlabel('Población Total')
plt.ylabel('Frecuencia')
plt.show()
# Comentario: Este histograma muestra la distribución de la población total por provincia.
# Puede ayudar a identificar las provincias con mayor o menor población.

# Visualización 2: Relación entre dos variables (Diagrama de dispersión)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='poblacion_varones', y='poblacion_mujeres', data=data, color='salmon')
plt.title('Relación entre Población de Varones y Mujeres por Provincia')
plt.xlabel('Población de Varones')
plt.ylabel('Población de Mujeres')
plt.show()
# Comentario: Este diagrama de dispersión muestra la relación entre la población de varones y mujeres por provincia.
# Puede ser útil para identificar patrones en la distribución de género en diferentes provincias.

# Visualización 3: Otra visualización a elección (Gráfico de barras)
plt.figure(figsize=(10, 6))
sns.barplot(x='provincia', y='poblacion_total', data=data, palette='pastel')
plt.title('Población Total por Provincia')
plt.xlabel('Provincia')
plt.ylabel('Población Total')
plt.xticks(rotation=45)
plt.show()
# Comentario: Este gráfico de barras muestra la población total por provincia.
# Puede proporcionar una comparación visual rápida de las poblaciones entre provincias.