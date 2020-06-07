from vehiculo import Vehiculo

class Nuevo(Vehiculo):
    __marca = 'Toyota'
    __version = ''
    def __init__(self, modelo, puertas, color, pb, version):
        super().__init__(modelo, puertas, color, pb)
        self.__version = version
    def __str__(self):
        return super().__str__() + "\nMarca: {}\nVersion: {}".format(self.__marca, self.__version)
    def ajuste(self):
        porcentaje = 0.1
        if self.__version.lower() == "full":
            porcentaje += 0.02
        return porcentaje
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo = self.getModelo(),
                            puertas = self.getPuertas(),
                            color = self.getColor(),
                            pb = self.getPB(),
                            version = self.__version
                            )
            )