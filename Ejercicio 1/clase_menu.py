class Menu(object):
    __switcher = None
    def __init__(self):
        self.__switcher = { 0: self.salir,
                            1: self.mostrarLibro,
                            2: self.buscarPalabra}
    def opcion(self, op, manejador):
        func=self.__switcher.get(op, lambda: print('Opción no válida'))
        func(manejador)
    def salir(self, manejador):
        pass
    def mostrarLibro(self, manejador):
        idLibro = int(input('Ingrese un ID de libro: '))
        manejador.mostrarLibro(idLibro)
    def buscarPalabra(self, manejador):
        palabra = input('Ingrese una palabra: ')
        manejador.buscarPalabra(palabra)