cuenta = {
    "nombre":"Pepe",
    "apellido":"Argento",
    "email":"pepe@gmail.com"
}

for datos in cuenta.items(): # key itera la clave e item el valor
    key = datos[0]
    value = datos[1]
    print(f"la clave es {key} y el valor es {value}")
