from agente import Agente

class PersonalApoyo(Agente):
    __categoria = 0
    def __init__(self, cuil, nombre, apellido, basico, antiguedad, categoria):
        super().__init__(cuil, nombre, apellido, basico, antiguedad)
        self.__categoria = categoria
    def aumento(self):
        if self.__categoria <= 10:
            porcentaje = 10
        elif self.__categoria <= 20:
            porcentaje = 20
        else:
            porcentaje = 30
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
                            categoria = self.__categoria
                            )
            )