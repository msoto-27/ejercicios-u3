from empleado_temporal import EmpleadoTemporal

class Contratado(EmpleadoTemporal):
    __horas = 0
    __valor = 150
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas):
        super().__init__(dni, nombre, direccion, telefono, fecha_inicio, fecha_fin)
        self.__horas = horas
    def setValor(self, valor):
        self.__valor = valor
    def sumarHoras(self, horas):
        self.__horas += horas
    def calcularSueldo(self):
        return self.__horas * self.__valor
