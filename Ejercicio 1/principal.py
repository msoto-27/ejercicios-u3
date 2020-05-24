from clase_menu import Menu
from clase_manejalibros import ManejaLibros

if __name__ == '__main__':
    menu = Menu()
    manejador = ManejaLibros()
    salir = False
    while not salir:
        print("======= MENU =======\n"
              "0 Salir\n"
              "1 Mostrar informacion de un libro\n"
              "2 Mostrar libros que contienen una determinada palabra en su titulo o en el titulo de uno de sus capitulos\n")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, manejador)
        salir = op == 0
