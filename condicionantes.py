# Condiciones para ser adulto, ser mayor de 18 años

edad=12
edad=21
if edad >= 18:
    print("sos mayor de edad")
else:
    print("sos menor de edad")

# Ingresos mensuales segun el lugar

ingreso_mensual=20000
gasto_mensual=22000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: # anidar un if dentro de otro if para agregar otra condicion
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000: # anidar un elif para agregar mas condiciones
        print("estas bien")
    else:                                       # anidar un else que arroja un resultado si no cumple la condicion
        print("estas gastando mucho")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en argentina")
elif ingreso_mensual > 100:
    print("estas bien en venezuela")
else:
    print("tus ingresos no son suficientes")



