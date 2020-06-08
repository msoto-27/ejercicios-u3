from docente import Docente
from investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria = ''
    __extra = 0
    def __init__(self, cuil, nombre, apellido, basico, antiguedad, carrera, cargo, catedra, area, tipo, categoria, extra):
        Docente.__init__(self, cuil, nombre, apellido, basico, antiguedad, carrera, cargo, catedra)#, area, tipo)
        Investigador.__init__(self, cuil, nombre, apellido, basico, antiguedad, area, tipo)
        
        self.__categoria = categoria
        self.__extra = extra
    def __str__(self):
        return super().__str__() + "\nCategoria de investigacion: {}\nImporte Extra: {}\n".format(self.__categoria, self.__extra)
    def getCategoria(self):
        return self.__categoria
    def getExtra(self):
        return self.__extra
    def aumento(self):
        return Docente.aumento(self) + self.__extra
    def mostrarExtra(self):
        return "Nombre: {}\nApellido: {}\nImporte extra: {}\n".format(self.getNombre(), self.getApellido(), self.__extra)
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil = self.getCUIL(),
                            nombre = self.getNombre(),
                            apellido = self.getApellido(),
                            basico = self.getBasico(),
                            antiguedad = self.getAntiguedad(),
                            carrera = self.getCarrera(),
                            cargo = self.getCargo(),
                            catedra = self.getCatedra(),
                            area = self.getArea(),
                            tipo = self.getTipo(),
                            categoria = self.__categoria,
                            extra = self.__extra
                            )
            )