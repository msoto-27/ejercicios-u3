from empleado_temporal import EmpleadoTemporal

class Externo(EmpleadoTemporal):
    __tarea = ''
    __monto_viatico = ''
    __costo = ''
    __monto_seguro = ''
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, tarea, monto_viatico, costo, monto_seguro):
        super().__init__(dni, nombre, direccion, telefono, fecha_inicio, fecha_fin)
        self.__tarea = tarea
        self.__monto_viatico = monto_viatico
        self.__costo = costo
        self.__monto_seguro = monto_seguro
    def getTarea(self):
        return self.__tarea
    def getCosto(self):
        return self.__costo
    def setViatico(self, monto_viatico):
        self.__monto_viatico = monto_viatico
    def calcularSueldo(self):
        return self.__costo - self.__monto_viatico - self.__monto_seguro
