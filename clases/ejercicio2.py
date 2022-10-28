def determinanterecursivo():
    a=float(input("seleccione el elemento 1x1: "))
    b=float(input("seleccione el elemento 1x2: "))
    c=float(input("seleccione el elemento 1x3: "))
    d=float(input("seleccione el elemento 2x1: "))
    e=float(input("seleccione el elemento 2x2: "))
    f=float(input("seleccione el elemento 2x3: "))
    g=float(input("seleccione el elemento 3x1: "))
    h=float(input("seleccione el elemento 3x2: "))
    i=float(input("seleccione el elemento 3x3: "))
    determinantrecursivo= a*e*i + d*h*c + b*f*g - c*e*g - b*d*i - a*f*h
    matriz = [[a, b, c], 
    [d, e, f], 
    [g, h, i]]
    print("su matriz es la siguiente: ", matriz )
    print("el determinante de su matriz es: ", determinantrecursivo)

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

def gauss():
    for z in range(3-1):
        for x in range(1, 3-z):
            if (matriz[z][z] !=0):
                p = matriz[x+z][z] / matriz[z][z]
                for y in range(3):
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)

def det():
    deter=1
    for x in range(3):
        deter = matriz[x][x]*deter
    print("El determinante de su matriz es: ", deter)

gauss()
det()
