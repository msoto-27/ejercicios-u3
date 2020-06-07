import zope

from icoleccion import IColeccion
from nodo import Nodo
from usado import Usado

@zope.interface.implementer(IColeccion)
class Lista(object):
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def __iter__(self):
        return self
    def __len__(self):
        return self.__tope
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__indice += 1
            self.__actual = self.__actual.getSiguiente()
            return dato
    def agregarElemento(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    def insertarElemento(self, elemento, posicion):
        if posicion == 0:
            self.agregarElemento(elemento)
        else:
            aux = self.__comienzo
            i = 0
            elemento = Nodo(elemento)
            while i < posicion and aux != None:
                anterior = aux
                aux = aux.getSiguiente()
                i += 1
            
            if i > posicion:
                raise IndexError
            else:
                elemento.setSiguiente(aux)
                anterior.setSiguiente(elemento)
                self.__tope += 1
    def mostrarElemento(self, posicion):
        if posicion < len(self):
            aux = self.__comienzo
            i = 0
            while i < posicion and aux != None:
                aux = aux.getSiguiente()
                i += 1
            return aux.getDato()
        else:
            raise IndexError
    def buscarUsado(self, patente):
        aux = self.__comienzo
        r = None
        while aux != None and r == None:
            if isinstance(aux.getDato(), Usado) and (aux.getDato().getPatente() == patente):
                r = aux.getDato()
            else:
                aux = aux.getSiguiente()
        return r
    def menorPrecio(self):
        minimo = 9999999
        vehiculo_minimo = None
        for i in self:
            importe_v = i.calcularPV()
            if importe_v < minimo:
                minimo = importe_v
                vehiculo_minimo = i
        return vehiculo_minimo
    def mostrar(self):
        for i in self:
            print(i.mostrarResumen() + "\n")
    def toJSON(self):
        vehiculos = []
        for i in self:
            vehiculos.append(i.toJSON())
        d = dict(__class__ = self.__class__.__name__, datos = vehiculos)
        return d