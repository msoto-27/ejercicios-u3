class Inscripcion(object):
    __fechaInscripcion = None
    __pago = False
    __persona = None
    __taller = None
    def __init__(self, fechaInscripcion, persona, taller):
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = False
        self.__persona = persona
        self.__taller = taller
    def getFecha(self):
        return self.__fechaInscripcion
    def getPago(self):
        return self.__pago
    def getPersona(self):
        return self.__persona
    def getTaller(self):
        return self.__taller
    def registrarPago(self):
        self.__pago = True
    def obtenerDeuda(self):
        if self.__pago:
            r = 0
        else:
            taller = self.__taller
            r = taller.getMonto()
        return r