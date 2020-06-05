import csv
import datetime
import numpy as np

from empleado import Empleado
from de_planta import Planta
from contratado import Contratado
from externo import Externo

class ColeccionEmpleado(object):
    __empleados = None
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

    def buscarEmpleadoContratado(self, dni):
        i = 0
        while i<len(self.__empleados) and self.__empleados[i].getDNI() != dni:
            i += 1
        if i<len(self.__empleados):
            if isinstance(self.__empleados[i], Contratado):
                r =  self.__empleados[i]
            else:
                print("El DNI ingresado no corresponde a un empleado contratado")
                r =  None
        else:
            print("El DNI ingresado no corresponde a ningun empleado")
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
        for i in self.__empleados:
            if i.calcularSueldo() < 25000:
                print(i)
    def mostrarSueldos(self):
        for i in self.__empleados:
            print(i.mostrarSueldo())
            

"""a = ColeccionEmpleado(3)
b = a.getEmpleados()
print(b[0].getDNI())"""