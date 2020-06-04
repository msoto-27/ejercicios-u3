from clase_inscripcion import Inscripcion

class TallerCapacitacion(object):
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0
    __inscripciones = None
    def __init__(self, idTaller, nombre, vacantes, montoInscripcion):
        self.__idTaller = idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = montoInscripcion
        self.__inscripciones = []
    def getID(self):
        return self.__idTaller
    def getNombre(self):
        return self.__nombre
    def getVacantes(self):
        return self.__vacantes
    def getMonto(self):
        return self.__montoInscripcion
    def getInscripciones(self):
        return self.__inscripciones
    def inscribirPersona(self, fecha, persona):
        inscripcion = Inscripcion(fecha, persona, self)
        self.__inscripciones.append(inscripcion)
        self.__vacantes -= 1
        return inscripcion