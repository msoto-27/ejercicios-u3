import csv
import numpy as np
from clase_inscripcion import Inscripcion

class ColeccionInscripcion(object):
    __inscripciones = None
    __dimension = 0
    def __init__(self):
        self.__inscripciones = np.empty(0, dtype=Inscripcion)
        self.__dimension = 0
    def agregarInscripcion(self, inscripcion):
        self.__dimension += 1
        self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__dimension - 1] = inscripcion
    def buscarPorPersona(self, persona):
        i = 0
        while self.__inscripciones[i].getPersona() != persona:
            i += 1
        return self.__inscripciones[i] #Si la persona existe, entonces es 100% seguro que su inscripcion exista
    def guardarInscripciones(self):
        archivo = open("inscripciones.csv", "w")
        writer = csv.writer(archivo)
        
        for i in self.__inscripciones:
            dni = i.getPersona().getDNI()
            id_taller = i.getTaller().getID()
            fecha = i.getFecha()
            pago = i.getPago()
            writer.writerow([dni, id_taller, fecha, pago])
        archivo.close()