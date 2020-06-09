import csv
import datetime
import zope
import numpy as np

from zope.interface import implementer
from empleado import Empleado
from de_planta import Planta
from contratado import Contratado
from externo import Externo
from itesorero import ITesorero
from igerente import IGerente


@implementer(ITesorero)
@implementer(IGerente)
class ColeccionEmpleado(object):
    __empleados = None
    __tope = 0
    def __init__(self, dimension):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        archivo = open("planta.csv")
        reader = csv.reader(archivo)
        n = 0
        for i in reader:
          self.__empleados[n] = Planta(i[0], i[1], i[2], i[3], int(i[4]), int(i[5]))
          n += 1
        archivo = open("contratados.csv")
        reader = csv.reader(archivo)
        for i in reader:
            self.__empleados[n] = Contratado(i[0], i[1], i[2], i[3], datetime.date.fromisoformat(i[4]), datetime.date.fromisoformat(i[5]), int(i[6]))
            n += 1
        archivo = open("externos.csv")
        reader = csv.reader(archivo)
        for i in reader:
            self.__empleados[n] = Externo(i[0], i[1], i[2], i[3], datetime.date.fromisoformat(i[4]), datetime.date.fromisoformat(i[5]), i[6], int(i[7]), int(i[8]), int(i[9]))
            n += 1
        self.__tope = len(self.__empleados)
    def buscarEmpleado(self, dni):
        i = 0
        while i<len(self.__empleados) and self.__empleados[i].getDNI() != dni:
            i += 1
        if i<len(self.__empleados):
            r = self.__empleados[i]
        else:
            print("El DNI ingresado no corresponde a ningun empleado")
            r = None
        return r
    def buscarEmpleadoContratado(self, dni):
        e = self.buscarEmpleado(dni)
        if e:
            if isinstance(e, Contratado):
                r =  e
            else:
                print("El DNI ingresado no corresponde a un empleado contratado")
                r =  None
        else:
            r = None
        return r
    
    def totalTarea(self, tarea):
        f_actual = datetime.date.today() # Obtiene la fecha de hoy
        t = 0
        
        for i in self.__empleados:
            if isinstance(i, Externo):
                if tarea == i.getTarea() and f_actual < i.getFechaFin():
                    t += i.getCosto()
        return t
    def mostrarSegunSueldo(self):
        for i in range(self.__tope):
            if self.__empleados[i].calcularSueldo() < 25000:
                print(i)
    def mostrarSueldos(self):
        for i in range(self.__tope):
            print(self.__empleados[i].mostrarSueldo())
            
    # Metodo Tesorero
    def gastosSueldoPorEmpleado(self, dni):
        e = self.buscarEmpleado(dni)
        if e:
            print("El gasto por sueldos del empleado seleccionado es de: $", e.calcularSueldo())
    # Metodos Gerente
    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        e = self.buscarEmpleado(dni)
        if e:
            if isinstance(e, Planta):
                e.setBasico(nuevoBasico)
            else:
                print("El DNI ingresado no corresponde a un empleado de planta")
    def modificarViaticoEExterno(self, dni, nuevoViatico):
        e = self.buscarEmpleado(dni)
        if e:
            if isinstance(e, Externo):
                e.setViatico(nuevoViatico)
            else:
                print("El DNI ingresado no corresponde a un empleado externo")
    def modificarValorEPorHora(self, dni, nuevoValorHora):
        e = self.buscarEmpleado(dni)
        if e:
            if isinstance(e, Contratado):
                e.setValor(nuevoValorHora)
            else:
                print("El DNI ingresado no corresponde a un empleado externo")