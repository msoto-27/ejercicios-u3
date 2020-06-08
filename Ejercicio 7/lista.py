import zope

from icoleccion import IColeccion
from nodo import Nodo
from investigador import Investigador
from docente_investigador import DocenteInvestigador

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
            dato = self.__actual.getDato() # Muestra el dato del nodo en las iteraciones
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
    def listadoCarrera(self, carrera):
        aux = Lista()
        for i in self:
            if isinstance(i, DocenteInvestigador) and i.getCarrera() == carrera:
                nombre = i.getNombre()
                j = 0
                while j < len(aux) and nombre >= aux.mostrarElemento(j).getNombre():
                    j += 1
                aux.insertarElemento(i, j)
        return aux
    def contarInvestigadores(self, area):
        inv = 0
        docinv = 0
        for i in self:
            if isinstance(i, Investigador) or isinstance(i, DocenteInvestigador):
                if i.getArea() == area:
                    if isinstance(i, DocenteInvestigador):
                        docinv += 1
                    else:
                        inv += 1
        return inv, docinv
    def mostrarSueldos(self):
        lista_aux = Lista()
        for i in self:
            aux = i.getApellido()
            j = 0
            while j < len(lista_aux) and aux >= lista_aux.mostrarElemento(j).getApellido():
                j += 1
            lista_aux.insertarElemento(i, j)
        for i in lista_aux:
            print(i.mostrarResumen())
    def listadoCategoria(self, categoria):
        t = 0
        print("Lista de docentes investigadores del area seleccionada:\n")
        for i in self:
            aux = i
            if isinstance(aux, DocenteInvestigador) and aux.getCategoria() == categoria:
                print(aux.mostrarExtra())
                t += aux.getExtra()
        return t
    def toJSON(self):
        personal = []
        for i in self:
            personal.append(i.toJSON())
        d = dict(__class__ = self.__class__.__name__, datos = personal)
        return d
    
