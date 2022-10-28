vehiculos=[{"nombre": "AT-AT", "longitud": 35, "tripulacion": 70, "cantidad de pasajeros": 150}, 
{"nombre": "halcon milenario", "longitud": 20, "tripulacion": 5, "cantidad de pasajeros": 30},
{"nombre": "estrella de la muerte", "longitud": 1000000, "tripulacion": 7000, "cantidad de pasajeros": 1500000000},
{"nombre": "AT-ST", "longitud": 15, "tripulacion": 5, "cantidad de pasajeros": 12},
{"nombre": "X-WING", "longitud": 10, "tripulacion": 4, "cantidad de pasajeros": 1},
{"nombre": "A-WING", "longitud": 11, "tripulacion": 3, "cantidad de pasajeros": 2}
]


print("los datos del halcon milenario son: ", vehiculos[2])
print("los datos de la estrella de la muerte son: ", vehiculos[3])


lista=[]
for i in range(0, 6):
    a=vehiculos[i].get('tripulacion')
    lista.append(a)
a=max(lista)
print("el maximo de cantidad de tripulacion es: ", max(lista))
print(lista)
print(a, "es la cantidad de tripulacion de: ", vehiculos[2].get("nombre"))


lista2=[]
lista3=[]
for i in range(0, 6):
    z=vehiculos[i].get('cantidad de pasajeros')
    lista2.append(z)
b=min(lista2)
print("el minimo de cantidad de pasajeros es", b)
for i in range(0, 6):
    c=vehiculos[i]. get('cantidad de pasajero')
    if c>=b:
        d=vehiculos[i].get('nombre')
        lista3.append(d)
print("Los 5 vehiculos con mas tripulacion son: ", lista3)

lista7=[lista]
for i in range(0, 6):
    g=vehiculos[z].get('cantidad de pasajeros')
    if g>=1:
        h=vehiculos.get('nombre')
        lista7.append(h)
