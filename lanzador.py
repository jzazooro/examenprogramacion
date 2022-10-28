from clases.ejercicio2 import determinanterecursivo
from clases.ejercicio2 import gauss
from clases.ejercicio2 import det

determinanterecursivo()

a=float(input("seleccione el elemento 1x1: "))
b=float(input("seleccione el elemento 1x2: "))
c=float(input("seleccione el elemento 1x3: "))
d=float(input("seleccione el elemento 2x1: "))
e=float(input("seleccione el elemento 2x2: "))
f=float(input("seleccione el elemento 2x3: "))
g=float(input("seleccione el elemento 3x1: "))
h=float(input("seleccione el elemento 3x2: "))
i=float(input("seleccione el elemento 3x3: "))
matriz=[[a, b, c], 
[d, e, f], 
[g, h, i]]

gauss()
det()


