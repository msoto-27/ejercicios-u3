class Empleado(object):
    __dni = ''
    __nombre = ''
    __direccion = ''
    __telefono = ''
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    def getDNI(self):
        return self.__dni
    def __str__(self):
        return "Nombre: {}\nTipo de empleado: {}\nDireccion: {}\nDNI: {}\n".format(self.__nombre, self.__class__.__name__, self.__direccion, self.__dni)
    def calcularSueldo(self):
        pass
    def mostrarSueldo(self):
        return "Nombre: {}\nTipo de empleado: {}\nTelefono: {}\nSueldo: {}\n".format(self.__nombre, self.__class__.__name__, self.__telefono, self.calcularSueldo())
