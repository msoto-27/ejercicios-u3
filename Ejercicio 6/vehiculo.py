import abc
from abc import ABC

class Vehiculo(ABC):
    __modelo = ''
    __puertas = 0
    __color = ''
    __pb = 0
    def __init__(self, modelo, puertas, color, pb):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__pb = pb
    def __str__(self):
        return "Modelo: {}\nCantidad de puertas: {}\nColor: {}\nPrecio base: {:.2f}".format(self.__modelo, self.__puertas, self.__color, self.__pb)
    def getModelo(self):
        return self.__modelo
    def getPuertas(self):
        return self.__puertas
    def getColor(self):
        return self.__color
    def getPB(self):
        return self.__pb
    def setPB(self, pb):
        self.__pb = pb
    def mostrarResumen(self):
        return "Modelo: {} | Cantidad de puertas: {} | Precio de venta: {:.2f}".format(self.__modelo, self.__puertas, self.calcularPV())
    @abc.abstractmethod
    def ajuste(self):
        pass
    def calcularPV(self):
        return self.__pb + self.__pb * self.ajuste()