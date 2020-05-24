class Libro(object):
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __lsbn = 0
    __cantidadCapitulos = 0
    __capitulos = []
    def __init__(self, idLibro, titulo, autor, editorial, lsbn, cantidadCapitulos):
        self.__idLibro =idLibro
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__lsbn = lsbn
        self.__cantidadCapitulos = cantidadCapitulos
        self.__capitulos = []
    def setCapitulo(self, capitulo):
        self.__capitulos.append(capitulo)
    def getIdLibro(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getCapitulos(self):
        return self.__capitulos
    def getTotalPaginas(self):
        c = 0
        for i in self.__capitulos:
            c += i.getCantidadPaginas()
        return c