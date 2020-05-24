import csv

from clase_libro import Libro
from clase_capitulo import Capitulo

class ManejaLibros(object):
    __lista_libros = []
    def __init__(self):
        archivo = open('libros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        i = -1
        for fila in reader:
            if len(fila) == 6:
                self.__lista_libros.append(Libro(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5])))
                i += 1
            else:
                self.__lista_libros[i].setCapitulo(Capitulo(fila[0], int(fila[1])))
        archivo.close()
        
    def mostrarLibro(self, idLibro):
        i = 0
        longitud = len(self.__lista_libros)
        while i < longitud and self.__lista_libros[i].getIdLibro() != idLibro:
            i += 1
        if i < longitud:
            print('Titulo del libro:\n', self.__lista_libros[i].getTitulo())
            print('Cantidad de paginas:\n', self.__lista_libros[i].getTotalPaginas())
            print('Capitulos del libro:')
            for i in self.__lista_libros[i].getCapitulos():
                print(i.getTitulo())
        else:
            print('Libro no encontrado')
            
    def buscarPalabra(self, palabra):
        print('Libros que contienen "', palabra, '":\n')
        for i in self.__lista_libros:
            if palabra.lower() in i.getTitulo().lower():
                print('Libro: {} \nAutor: {}\n'.format(i.getTitulo(), i.getAutor()))
            else:
                j = 0
                lista_capitulos = i.getCapitulos()
                longitud = len(lista_capitulos)
                while j < longitud and palabra.lower() not in lista_capitulos[j].getTitulo().lower():
                    j += 1
                if j < longitud:
                    print('Libro: {} \nAutor: {}\n'.format(i.getTitulo(), i.getAutor()))