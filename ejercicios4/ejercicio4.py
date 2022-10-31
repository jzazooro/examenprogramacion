class Nave:
    def __init__(self, nombre, largo, trip, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.trip = trip
        self.pasajeros = pasajeros
    
    def __str__(self):
        return "{}, {}, {}, {}".format(self.nombre, self.largo, self.trip, self.pasajeros)
    
    def get_largo(self):
        return self.largo
    
    def diccionario(self):
        diccionario = {"Nombre": self.nombre , "Largo": self.largo , "Tripulacion": self.trip , "Pasajeros": self.pasajeros}
        return diccionario

class Naves:
    def __init__(self):
        self.naves = []
    
    def naves_append(self, nave):
        self.naves.append(nave)

    def get_Nombres(self, lista, key):
        "Metodo para obtener los nombres"
        lista2 = []
        for i in lista:
            for n in self.naves:
                if n[key] == i:
                    lista2.append(n["Nombre"]) 
        return lista2        

    def lis_largo(self):
        "Ordena las naves segun el largo"
        lista = []
        for i in self.naves:
            lista.append(i["Largo"])
        lista.sort(reverse=True)
        return self.get_Nombres(lista, "Largo")
    
    def lis_nombre(self):
        "Ordena las naves segun el nombre"
        lista = []
        for i in self.naves:
            lista.append(i["Nombre"])
        lista.sort()
        return lista
    
    def cantidad_pasajeros(self):
        "Determina las 5 naves con mayor cantidad de pasajeros"
        lista = []
        for i in self.naves:
            lista.append(i["Pasajeros"])
        lista.sort()
        return self.get_Nombres(lista, "Pasajeros")[0:5]
    
    def mayor_trip(self):
        "Determina la nave con mayor tripulacion"
        lista = []
        for i in self.naves:
            lista.append(i["Tripulacion"])
        lista.sort()
        return self.get_Nombres(lista, "Tripulacion")[0:1]

    def at(self):
        "Determina las naves que empiezan por AT"
        naves_nombre = self.lis_nombre()
        lista_nombres = []
        for i in naves_nombre:
            if i[0:2] == "AT":
                lista_nombres.append(i)
            else:
                pass
        if len(lista_nombres) == 0:
            return None
        else:
            return lista_nombres
    
    def pasajeros_6_o_mas(self):
        "Determina las naves que pueden contener 6 pasajeros o mas"
        #Reutilizamos el codigo del metodo cantidad_pasajeros
        lista = []
        for i in self.naves:
            if i["Pasajeros"] >= 6:
                lista.append(i["Pasajeros"])
        return self.get_Nombres(lista, "Pasajeros")
    
    def naves_peq_grand(self):
        "Muestra la informacion de la nave mas pequeña y la mas grande"
        #Reutilzamos el codigo del metodo lis_largo
        lista = []
        for i in self.naves:
            lista.append(i["Largo"])
        lista.sort()
        for i in self.naves:
            if lista[0] == i["Largo"]:
                print(i)
            elif lista[len(lista)-1] == i["Largo"]:
                print(i)
            else:
                pass

def main3():

    nave1 = Nave("Halcon Milenario",5, 100, 67)
    nave2 = Nave("Estrella de la Muerte", 6, 75, 50)
    nave3 = Nave("Pepe", 3, 30, 12)
    nave4 = Nave("Pelayo", 4, 45, 34)
    nave5 = Nave("Esthernon", 4, 55, 31)
    nave6 = Nave("Terepe", 3, 30, 10)


    print(nave1)
    print(nave2)


    lista_naves = [nave1, nave2, nave3, nave4, nave5, nave6]
    ejercito = Naves()
    for i in lista_naves:
        ejercito.naves_append(i.diccionario())

    

    print(ejercito.lis_nombre())
    print(ejercito.cantidad_pasajeros())
    print(ejercito.mayor_trip())
    print(ejercito.at())
    print(ejercito.pasajeros_6_o_mas())
    print(ejercito.naves_peq_grand())
main3()