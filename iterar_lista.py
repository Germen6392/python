# Bucle for in
lista_mercado = ["cereal","yogur","pan","queso"]
for producto in lista_mercado:
    print(f"hay que ir al super y comprar * {producto}")

# horas trabajadas - pago por hora usando zip para los dias y multiplicando por hora
horas = [2,3,5,2]
dias = ["Martes","Miercoles","Jueves","Viernes"]
for num in range(20,24): # usando range repito la cantidad de veces que se repita la frase
    for hora,dia in zip(horas,dias):
        pago = hora * 150
        print(f"El dia {dia} cobrare $ {pago}")
