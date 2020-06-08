import abc
from abc import ABC

class Agente(ABC):
    __cuil = ''
    __nombre = ''
    __apellido = ''
    __basico = 0
    __antiguedad = 0
    def __init__(self, cuil, nombre, apellido, basico, antiguedad, carrera='', cargo='', catedra='', area='', tipo=''):
        self.__cuil = cuil
        self.__nombre = nombre
        self.__apellido = apellido
        self.__basico = basico
        self.__antiguedad = antiguedad
    def __str__(self):
        return "Nombre: {}\nApellido: {}\nCuil: {}\nSueldo Basico: {}\nAnios de antiguedad: {}".format(self.__nombre, self.__apellido, self.__cuil, self.__basico, self.__antiguedad)
    def getCUIL(self):
        return self.__cuil
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getBasico(self):
        return self.__basico
    def getAntiguedad(self):
        return self.__antiguedad
    def mostrarResumen(self):
        return "Apellido: {}\nNombre: {}\nTipo de Agente: {}\nSueldo: {}\n".format(self.__apellido, self.__nombre, {"PersonalApoyo":"Personal de Apoyo", "Docente":"Docente", "Investigador":"Investigador", "DocenteInvestigador":"Docente Investigador"}[self.__class__.__name__], self.calcularSueldo())
    @abc.abstractmethod
    def aumento(self):
        pass
    def calcularSueldo(self):
        return self.__basico + self.__basico * (self.__antiguedad * 0.01) + self.aumento()
