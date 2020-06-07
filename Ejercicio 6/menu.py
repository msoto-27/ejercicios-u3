from object_encoder import ObjectEncoder
from lista import Lista
from nuevo import Nuevo
from usado import Usado

class Menu(object):
    __lista = None
    __switcher = None
    def __init__(self):
        obj = ObjectEncoder()
        self.__lista = obj.decodificar(obj.cargar())
        self.__switcher = {1:self.opcion1, 2:self.opcion2, 3:self.opcion3, 4:self.opcion4, 5:self.opcion5, 6:self.opcion6, 7:self.opcion7, 0:self.salir}
    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func()
    def salir(self):
        print("Fin del programa")
    def __crearVehiculo(self):
        modelo = input("Ingrese el modelo del vehiculo: ")
        puertas = int(input("Ingrese la cantidad de puertas: "))
        color = input("Ingrese el color: ")
        pb = float(input("Ingrese el precio base: "))
        
        flag = False
        while not flag:
            condicion = input("Ingrese 'N' si el vehiculo es nuevo; 'U' si es usado: ").lower()
            if condicion == 'n':
                version = input("Ingrese la version (base o full) : ")
                vehiculo = Nuevo(modelo, puertas, color, pb, version)
                flag = True
            elif condicion == 'u':
                marca = input("Ingrese la marca: ")
                patente = input("Ingrese la patente: ")
                anio = int(input("Ingrese el anio: "))
                km = int(input("Ingrese el kilometraje: "))
                vehiculo = Usado(modelo, puertas, color, pb, marca, patente, anio, km)
                flag = True
            else:
                print("Opcion no valida")
        return vehiculo
    def opcion1(self):
        vehiculo = self.__crearVehiculo()
        pos = int(input("Ingrese la posicion: "))
        try:
            self.__lista.insertarElemento(vehiculo, pos-1)
            print("Vehiculo insertado correctamente")
        except IndexError:
            print("Posicion no valida")
    def opcion2(self):
        vehiculo = self.__crearVehiculo()
        self.__lista.agregarElemento(vehiculo)
        print("Vehiculo insertado correctamente")
    def opcion3(self):
        pos = int(input("Ingrese una posicion: "))
        try:
            vehiculo = self.__lista.mostrarElemento(pos-1)
        except IndexError:
            print("Posicion no valida")
        else:
            if isinstance(vehiculo, Nuevo):
                print("El vehiculo en la posicion ingresada es nuevo")
            else:
                print("El vehiculo en la posicion ingresada es usado")
    def opcion4(self):
        patente = input("Ingrese la patente de un vehiculo: ")
        vehiculo = self.__lista.buscarUsado(patente)
        while not vehiculo:
            print("El vehiculo no ha sido encontrado")
            patente = input("Ingrese la patente de un vehiculo: ")
            vehiculo = self.__lista.buscarUsado(patente)
        pb = float(input("Ingrese el nuevo precio base: "))
        vehiculo.setPB(pb)
        print("Nuevo precio de venta: {:.2f}".format(vehiculo.calcularPV()))
    def opcion5(self):
        vehiculo = self.__lista.menorPrecio()
        print("Informacion completa del vehiculo mas economico:\n")
        print(vehiculo)
    def opcion6(self):
        print("Lista de todos los vehiculos:\n")
        self.__lista.mostrar()
    def opcion7(self):
        obj = ObjectEncoder()
        obj.guardar(self.__lista.toJSON())
        print("Los datos han sido guardados")