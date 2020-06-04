import csv
import numpy as np
from clase_tallercapacitacion import TallerCapacitacion

class ColeccionTaller(object):
    __talleres = None
    __cantidad = 0
    def __init__(self):
        archivo = open("talleres.csv")
        reader = csv.reader(archivo)
        
        self.__cantidad = 0
        for i in reader:
            if len(i) == 1:
                self.__talleres = np.empty(int(i[0]), dtype=TallerCapacitacion)
            else:
                self.__talleres[self.__cantidad] = TallerCapacitacion(int(i[0]), i[1], int(i[2]), int(i[3]))
                self.__cantidad += 1
        archivo.close()
    def mostrarTalleres(self):
        print("Lista de talleres:\n"
              "ID Nombre")
        for i in self.__talleres:
            print(i.getID(), "", i.getNombre())
    def buscarTaller(self, id_taller):
        i = 0
        while i<self.__cantidad and id_taller != self.__talleres[i].getID():
            i += 1
        if i<self.__cantidad:
            r = self.__talleres[i]
        else:
            r = None
        return r
    
    
