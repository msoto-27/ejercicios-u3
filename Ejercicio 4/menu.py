from coleccion_empleado import ColeccionEmpleado

class Menu(object):
    __ce = None
    __switcher = None
    def __init__(self):
        dimension = int(input("Ingrese la cantidad de empleados (7) : ")) # 3
        self.__ce = ColeccionEmpleado(dimension)
        self.__switcher = {1:self.opcion1, 2:self.opcion2, 3:self.opcion3, 4:self.opcion4, 0:self.salir}
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