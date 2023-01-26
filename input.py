# Pedir nombre al usuario
nombre = input("ingresa tu nombre: ")

# mostrar info
print(f'tu nombre es: {nombre}')

# Pedir un numero entero y multiplicarlo por 2
numero = input("ingresa tu numero: ")
resultado = int(numero) * 2
# mostrar info
print(resultado)

# ingresar precio y sumar el iva
valor = input("ingresa el precio: ")
precio = float(valor)
iva = precio * 21 / 100
final = precio + iva
# mostrar info
print(final)
