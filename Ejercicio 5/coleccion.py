import numpy as np

from error_posicion import ErrorPosicion
from icoleccion import IColeccion
from zope.interface import implementer

@implementer(IColeccion)
class Coleccion(object):
    __arreglo = None
    def __init__(self):
        self.__arreglo = np.zeros(10, dtype=int)
    def insertarElemento(self, elemento, posicion):
        if 0 <= posicion < len(self.__arreglo):
            self.__arreglo[posicion] = elemento
            print("Arreglo:", self.__arreglo)
        else:
            raise ErrorPosicion(elemento)
    def agregarElemento(self, elemento):
        dimension = len(self.__arreglo)
        self.__arreglo.resize(dimension + 1)
        self.__arreglo[dimension] = elemento
        print("Arreglo:", self.__arreglo)
    def mostrarElemento(self, posicion):
        if 0 <= posicion < len(self.__arreglo):
            return "Numero: {}".format(self.__arreglo[posicion])
        else:
            raise ErrorPosicion(posicion)
            
        