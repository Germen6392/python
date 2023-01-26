# usar continue e if para saltear una iteraccion de una lista
frutas = ["banana","pera","manzana","naranja","durazno","rucula"] # rucula no es una fruta

for fruta in frutas:
    if fruta =="rucula": #marcamos la condicion que rucula no es una fruta
        continue #salteamos la iteraccion con continue
    print(f"Las frutas que vendemos son: {fruta}")
else:
    print("termina el bucle")

# usando break para cortar con el bucle
for fruta in frutas:
    if fruta =="naranja": #marcamos la condicion que se acabo el durazno y naranja
        break #corta el bucle en naranja
    print(f"Las frutas que vendemos son: {fruta}")

# duplicamos el precio de las frutas
precios = [100,140,200,400]
subida = [x*2 for x in precios]
print(subida)
