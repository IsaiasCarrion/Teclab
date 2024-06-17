import numpy as np
import pandas as pd
# 1 - Generar un array de 3 dimensiones y mostrar el output en una captura de pantalla.

# Creamos un array de 3 dimensiones con valores enteros aleatorios entre 1 y 10
array_3d = np.random.randint(1, 11, size=(3, 4, 5))

# Mostramos el array
print(array_3d)


# 2 - Ubicar el valor de un elemento en el array de 3 dimensiones con la función correspondiente y compartir el output en una captura de pantalla.
# Obtenemos el valor en la posición (1, 2, 3) del array
valor = array_3d[1, 2, 3]

# Mostramos el valor
print(valor)


# 3 - Utilizando append, agregamos 3 valores nuevos al array y compartamos output en una captura de pantalla
# Creamos un nuevo array con los valores que queremos agregar
nuevo_array = np.array([[[10], [11], [12]]])

# Agregamos el nuevo array al final de la tercera "profundidad" del array original
array_3d = np.append(array_3d, nuevo_array)

# Mostramos el array modificado
print(array_3d)


# 4 - Generar un nuevo array de 3 dimensiones, pero con el formato requerido para que el output en una captura de pantalla pueda mostrarnos un resultado como (3,3) usando shape
# Crear el array de 3 dimensiones
array_shape = np.arange(27).reshape((3, 3, 3))

# Verificar la forma del array
print("Forma del array:", array_shape.shape)

# Seleccionar una vista del array para mostrar como (3, 3)
print("Primera capa del array 3D:")
print(array_shape[0])


# 5- Ahora, con la librería de pandas, crear una serie llamada (marcas_productos) y compartir el output en una captura de pantalla donde pueda mostrarnos la lista.
# Crear la serie marcas_productos
marcas_productos = pd.Series(['Apple', 'Samsung', 'Sony', 'LG', 'Nokia', 'Huawei', 'Xiaomi',])

# Mostrar la serie
print(marcas_productos, '\n')


# 6 - Generar una nueva serie llamada (color_cantidad) utilizando index para generar o modiﬁcar la columna inicial. Luego, compartir el output en una captura de pantalla donde pueda mostrarnos la lista con los nombres de lacolumna. "Azul", "Blanco", "Celeste", "Negro", "Rojo".
# Crear la serie color_cantidad con índices específicos
color_cantidad = pd.Series([50, 30, 20, 40, 60], index=['Azul', 'Blanco', 'Celeste', 'Negro', 'Rojo'])

# Mostrar la serie
print(color_cantidad)

