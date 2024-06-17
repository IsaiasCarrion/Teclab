persona = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 34
}

# Consultar al usuario por la nacionalidad
nacionalidad = input("Ingrese la nacionalidad: ")

# Actualizar el diccionario (forma correcta)
persona["Nacionalidad"] = nacionalidad

# Mostrar información del usuario (incluyendo nacionalidad)
print(f"El nombre es {persona['Nombre']} {persona['Apellido']}, tiene {persona['Edad']} años, y es de nacionalidad {persona['Nacionalidad']}")