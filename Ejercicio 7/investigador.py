from agente import Agente

class Investigador(Agente):
    __area = ''
    __tipo = ''
    def __init__(self, cuil, nombre, apellido, basico, antiguedad, area, tipo):
        super().__init__(cuil, nombre, apellido, basico, antiguedad)
        self.__area = area
        self.__tipo = tipo
    def __str__(self):
        return super().__str__() + "\nArea: {}\nTipo: {}".format(self.__area, self.__tipo)
    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo
    def aumento(self):
        return 0
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil = self.getCUIL(),
                            nombre = self.getNombre(),
                            apellido = self.getApellido(),
                            basico = self.getBasico(),
                            antiguedad = self.getAntiguedad(),
                            area = self.__area,
                            tipo = self.__tipo
                            )
            )