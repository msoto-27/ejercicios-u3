class ErrorPosicion(Exception):
    __mensaje = ""
    __elemento = None
    def __init__(self, elemento):
        self.__mensaje = "ERROR: Posicion no valida"
        self.__elemento = elemento
    def getMensaje(self):
        return self.__mensaje
    def getElemento(self):
        return self.__elemento
    