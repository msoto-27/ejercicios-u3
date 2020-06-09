import os

from coleccion_empleado import ColeccionEmpleado


class Menu(object):
    __ce = None
    __cuenta = None
    __switcher = None
    def __init__(self):
        dimension = int(input("Ingrese la cantidad de empleados (7) : "))
        self.__ce = ColeccionEmpleado(dimension)
        self.__switcher = {1:self.opcion1,
                           2:self.opcion2,
                           3:self.opcion3,
                           4:self.opcion4,
                           5:self.opcion5,
                           0:self.salir}
        self.__cuenta = None
    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opcion incorrecta"))
        func()
    def salir(self):
        print("Fin del programa")
        
    def opcion1(self):
        dni = input("Ingrese el DNI de un empleado: ")
        empleado = self.__ce.buscarEmpleadoContratado(dni)
        while not empleado:
            dni = input("Ingrese el DNI de un empleado: ")
            empleado = self.__ce.buscarEmpleadoContratado(dni)
            
        horas = int(input("Ingrese la cantidad de horas trabajadas: "))
        empleado.sumarHoras(horas)
        print("Horas sumadas correctamente")
       
            
    def opcion2(self):
        tarea = input("Ingrese una tarea (carpinteria, electricidad o plomeria) : ")
        while tarea not in ["carpinteria", "electricidad", "plomeria"]:
            print("Tarea ingresada no valida")
            tarea = input("Ingrese una tarea (carpinteria, electricidad o plomeria) : ")
        print("El costo total de la tarea seleccionada es: $", self.__ce.totalTarea(tarea))
        
    def opcion3(self):
        print("Lista de empleado a los que les corresponde el plan de ayuda solidaria:\n")
        self.__ce.mostrarSegunSueldo()
    
    def opcion4(self):
        print("Informacion de empleados y sus sueldos:\n")
        self.__ce.mostrarSueldos()
        
    def opcionTesorero(self):
        dni = input("Ingrese el dni de un empleado: ")
        self.__ce.gastosSueldoPorEmpleado(dni)
    
    def opcionGerente(self, op):
        dni = input("Ingrese el dni de un empleado: ")
        nuevo = int(input("Ingrese el nuevo valor: "))
        d = {'A':self.__ce.modificarBasicoEPlanta,
             'B':self.__ce.modificarViaticoEExterno,
             'C':self.__ce.modificarValorEPorHora}
        d[op](dni, nuevo)
    def menuGerente(self):
        salir = False
        while not salir:
            os.system("cls")
            print("===== MENU GERENTES =====\n"
                  "A) Modificar sueldo basico de un empleado de planta\n"
                  "B) Modificar viatico de un empleado externo\n"
                  "C) Modificar valor por hora de un empleado contratado\n"
                  "D) Salir")
            op = input("Ingrese una opcion: ").upper()
            if op in ['A', 'B', 'C']:
                self.opcionGerente(op)
            salir = op == 'D'
    def iniciarSesion(self):
        usuario = input("Ingrese su usuario: ")
        contrasenia = input("Ingrese su contraseña: ")
        d = {("uTesorero","ag@74ck"):"tesorero", ("uGerente", "ufC77#!1"):"gerente"}
        try:
            self.__cuenta = d[(usuario, contrasenia)]
        except KeyError:
            print("Usuario y/o contraseña no validos")
        else:
            print("Sesion iniciada")
    
    def opcion5(self):
        func = {"tesorero":self.opcionTesorero,
                "gerente":self.menuGerente,
                None:self.iniciarSesion}[self.__cuenta]
        func()
    
    def mostrarOpciones(self):
        salir = False
        while not salir:
            os.system("cls")
            print("===== MENU DE OPCIONES =====\n"
                  "1) Registrar horas de un empleado contratado\n"
                  "2) Mostrar el costo total de una de las tareas no finalizadas hasta el dia de hoy\n"
                  "3) Mostrar los datos de aquellos empleados que recibiran el plan de ayuda solidaria (empleados con sueldo menor a $25000)\n"
                  "4) Mostrar los datos de todos los empleados junto con sus sueldos")
            print({None:"5) Iniciar sesion",
                   "tesorero": "5) Mostrar gastos en concepto de sueldos de un empleado",
                   "gerente": "5) Acceder al menu de gerentes"}[self.__cuenta])
            print("0) Salir")
            op = int(input("Ingrese una opcion: "))
            self.opcion(op)
            salir = op == 0