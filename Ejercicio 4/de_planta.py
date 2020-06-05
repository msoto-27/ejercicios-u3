from empleado import Empleado

class Planta(Empleado):
    __sueldo_basico = 0
    __antiguedad = 0
    def __init__(self, dni, nombre, direccion, telefono, sueldo_basico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad
    def calcularSueldo(self):
        return self.__sueldo_basico + (self.__sueldo_basico * 0.01) * self.__antiguedad
