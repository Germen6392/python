# creando diccionarios con dict
#diccionario = dict(nombre="German",oficio="programador")
#print(diccionario)

# creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","documento"]) # agrego clave con un valor nulo
print(diccionario)

# creando diccionarios con fromkeys() con varias claves y un mismo valor
diccionarios = dict.fromkeys("abcd"," tema 1")
print (diccionarios)
