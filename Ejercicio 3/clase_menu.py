import datetime

from clase_persona import Persona
from clase_coleccionpersona import ColeccionPersona
from clase_colecciontaller import ColeccionTaller
from clase_coleccioninscripcion import ColeccionInscripcion

class Menu(object):
    __switcher = None
    __cpersona = None
    __ctaller = None
    def __init__(self):
        self.__switcher = {0:self.salir, 1:self.opcion1, 2:self.opcion2, 3:self.opcion3, 4:self.opcion4, 5:self.opcion5}
        self.__cpersona = ColeccionPersona()
        self.__ctaller = ColeccionTaller()
        self.__cinscripcion = ColeccionInscripcion()
    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func()

    def salir(self):
        print("Fin del programa")

    def opcion1(self):
        nombre = input("Ingrese el nombre de la persona: ")
        direccion = input("Ingrese la direccion de la persona: ")
        dni = input("Ingrese el DNI de la persona: ")
        nueva_persona = Persona(nombre, direccion, dni)
        self.__cpersona.agregarPersona(nueva_persona)
        
        self.__ctaller.mostrarTalleres()
        id_taller = int(input("Ingrese el ID del taller a inscribirse: "))
        taller = self.__ctaller.buscarTaller(id_taller)
        while not taller:
            print("ID ingresada no encontrada")
            self.__ctaller.mostrarTalleres()
            id_taller = int(input("Ingrese el ID del taller a inscribirse: "))
            taller = self.__ctaller.buscarTaller(id_taller)
            
        if taller.getVacantes():
            anio = int(input("Ingrese el año de inscripcion: "))
            mes = int(input("Ingrese el mes de inscripcion: "))
            dia = int(input("Ingrese el dia de inscripcion: "))
            fecha = datetime.date(anio, mes, dia)
            inscripcion = taller.inscribirPersona(fecha, nueva_persona)
            self.__cinscripcion.agregarInscripcion(inscripcion)
            print("Inscripcion realizada exitosamente")
        else:
            print("El taller seleccionado ya no tiene mas vacantes")

    def opcion2(self):
        dni = input("Ingrese el DNI de una persona: ")
        persona = self.__cpersona.buscarPorDNI(dni)
        if persona:    
            inscripcion = self.__cinscripcion.buscarPorPersona(persona)
            taller = inscripcion.getTaller()
            print("La persona con el DNI ingresado esta inscripta en el taller:", taller.getNombre())
            print("El monto que adeuda es de: $", inscripcion.obtenerDeuda())
        else:
            print("El DNI ingresado no corresponde al de ninguna persona registrada")
            
    def opcion3(self):
        id_taller = int(input("Ingrese el ID de un taller: "))
        taller = self.__ctaller.buscarTaller(id_taller)
        while not taller:
            print("ID ingresada no encontrada")
            id_taller = int(input("Ingrese el ID de un taller: "))
            taller = self.__ctaller.buscarTaller(id_taller)
        print("Datos de las personas inscriptas al taller:\n")
        for i in taller.getInscripciones():
            print(i.getPersona(), "\n")

    def opcion4(self):
        dni = input("Ingrese el DNI de una persona: ")
        persona = self.__cpersona.buscarPorDNI(dni)
        while not persona:
            print("DNI ingresado no registrado")
            dni = input("Ingrese el DNI de una persona: ")
            persona = self.__cpersona.buscarPorDNI(dni)
        inscripcion = self.__cinscripcion.buscarPorPersona(persona)
        inscripcion.registrarPago()
        print("El pago ha sido registrado")
    
    def opcion5(self):
        self.__cinscripcion.guardarInscripciones()
        print("La informacion de las inscripciones ha sido guardada en el archivo 'inscripciones.csv'")
        