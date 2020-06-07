import datetime

from vehiculo import Vehiculo

class Usado(Vehiculo):
    __marca = ''
    __patente = ''
    __anio = 0
    __km = 0
    def __init__(self, modelo, puertas, color, pb, marca, patente, anio, km):
        super().__init__(modelo, puertas, color, pb)
        self.__marca = marca
        self.__patente = patente
        self.__anio = anio
        self.__km = km
    def __str__(self):
        return super().__str__() + "\nMarca: {}\nPatente: {}\nAnio: {}\nKilometraje: {}".format(self.__marca, self.__patente, self.__anio, self.__km)
    def ajuste(self):
        porcentaje = (datetime.date.today().year - self.__anio) * 0.01
        if self.__km > 100000:
            porcentaje += 0.02
        return -porcentaje
    def getPatente(self):
        return self.__patente
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo = self.getModelo(),
                            puertas = self.getPuertas(),
                            color = self.getColor(),
                            pb = self.getPB(),
                            marca = self.__marca,
                            patente = self.__patente,
                            anio = self.__anio,
                            km = self.__km
                            )
        )
                            
                            
                            
                            
                            
        