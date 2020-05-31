import os

from clase_manejahelados import ManejaHelados
from clase_manejasabores import ManejaSabores

class Menu(object):
    __switcher = None
    __ms = None
    __mh = None
    def __init__(self):
        self.__switcher = {1:self.opcion1,
                      2:self.opcion2,
                      3:self.opcion3,
                      4:self.opcion4,
                      0:self.salir}
        self.__ms = ManejaSabores()
        self.__mh = ManejaHelados()
    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func()
    def salir(self):
        os.system("cls")
        print("Fin de la operacion")
    def opcion1(self):
        tipos = [100, 150, 250, 500, 1000]
        os.system("cls")
        tipo = int(input("Ingrese el tipo de helado segun su peso en gramos: "))
        while tipo not in tipos:
            os.system("cls")
            print("Tipo de helado no disponible")
            tipo = int(input("Ingrese el tipo de helado segun su peso en gramos: "))

        sabores = []
        lon = self.__ms.getLongitudLista()
        ban = False
        os.system("cls")
        
        while not ban and len(sabores) < 4:
            print("LISTA DE SABORES")
            print(" N°|          Nombre | Descripcion")
            print(self.__ms.mostrarSabores())
            print("Cantidad de sabores elegidos: {}/4".format(len(sabores)))
            numero = int(input("Ingrese el numero de un sabor o finalice con '0': "))
            os.system("cls")
            while not 0 <= numero <= lon:
                os.system("cls")
                print("El numero no se corresponde con ningun sabor")
                print("LISTA DE SABORES")
                print(" N°        Nombre              Descripcion")
                print(self.__ms.mostrarSabores())
                print("Cantidad de sabores elegidos: {}/4".format(len(sabores)))
                numero = int(input("Ingrese el numero de un sabor o finalice con '0': "))
            if numero == 0:
                if len(sabores) > 0:
                    ban = True
                else:
                    os.system("cls")
                    print("Seleccione al menos un sabor")
            else:
                sabor = self.__ms.getSabor(numero - 1)
                sabores.append(sabor)
        self.__mh.registrarPedido(tipo, sabores)

    def opcion2(self):
        lon = self.__ms.getLongitudLista()
        lista = self.__mh.contarSabores(lon)

        os.system("cls")
        print("Sabores mas vendidos:")
        c = 1
        for i in lista:
            print(c, ".", self.__ms.getSabor(i-1))
            c += 1
        input()
        os.system("cls")

    def opcion3(self):
        lon = self.__ms.getLongitudLista()
        os.system("cls")
        numero = int(input("Ingrese el numero de un sabor: "))
        while not 0 < numero <= lon:
                os.system("cls")
                print("El numero no se corresponde con ningun sabor")
                numero = int(input("Ingrese el numero de un sabor: "))
        sabor = self.__ms.getSabor(numero - 1)
        os.system("cls")
        print("El total estimado de gramos vendidos es de:", self.__mh.estimarTotalGramos(sabor))
        input()
        os.system("cls")

    def opcion4(self):
        tipos = [100, 150, 250, 500, 1000]
        os.system("cls")
        tipo = int(input("Ingrese el tipo de helado segun su peso en gramos: "))
        
        while tipo not in tipos:
            os.system("cls")
            print("Tipo de helado no disponible")
            tipo = int(input("Ingrese el tipo de helado segun su peso en gramos: "))

        lista = self.__mh.mostrarSaboresPorTipo(tipo)
        os.system("cls")
        if lista:
            print("LISTA DE SABORES")
            for i in lista:
                print(i)
        else:
            print("Ningun helado de ese tipo ha sido vendido")
        input()
        os.system("cls")
