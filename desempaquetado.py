datos = ["German","Rodriguez",2000] # lista
nombre,apellido,salario = datos
print(f"nombre: {nombre}")
print(f"apellido: {apellido}")
print(f"salario en pesos: ${salario}")

# transformar una lista en una tupla
tupla = tuple(datos) # la funcion tuple convierte una lista en tupla
print(tupla)

# maneras distintas de escribir una tupla
tupla1 = "denisse","esposa" # se puede escribir sin parentesis separando valores con coma
tupla2= "programador", # se puede agregar tupla de un solo valor finalizando con coma
print(tupla1)
print(type(tupla2))
