from agente import Agente

class Docente(Agente):
    __carrera = ''
    __cargo = ''
    __catedra = ''
    def __init__(self, cuil, nombre, apellido, basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, nombre, apellido, basico, antiguedad, area='', tipo='')
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    def __str__(self):
        return super().__str__() + "\nCarrera: {}\nCargo: {}\nCatedra: {}".format(self.__carrera, self.__cargo, self.__catedra)
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def aumento(self):
        if self.__cargo == "simple":
            porcentaje = 10
        elif self.__cargo == "semi-exclusivo":
            porcentaje = 20
        else:
            porcentaje = 50
        return super().getBasico() * (porcentaje * 0.01)
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil = self.getCUIL(),
                            nombre = self.getNombre(),
                            apellido = self.getApellido(),
                            basico = self.getBasico(),
                            antiguedad = self.getAntiguedad(),
                            carrera = self.__carrera,
                            cargo = self.__cargo,
                            catedra = self.__catedra
                            )
            )
                            