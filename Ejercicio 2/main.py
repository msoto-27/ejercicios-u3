from clase_manejahelados import ManejaHelados
from clase_menu import Menu

if __name__ == '__main__':
    manejador = ManejaHelados()
    menu = Menu()

    salir = False
    while not salir:
        print("1 Registrar pedido\n"
              "2 Mostrar los 5 helados mas pedidos\n"
              "3 Mostrar la cantidad de gramos pedida de un sabor de helado\n"
              "4 Mostrar todos los sabores vendidos de un tipo de helado en concreto\n"
              "0 Salir\n")
        op = int(input("Ingrese una opcion: "))
        menu.opcion(op)
        salir = op == 0
        