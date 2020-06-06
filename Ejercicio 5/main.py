from zope.interface import Interface

from coleccion import Coleccion
from icoleccion import IColeccion
from error_posicion import ErrorPosicion

def Interface(coleccion):
    flag = False
    while not flag:
        print("1) Insertar numero\n"
              "2) Agregar numero al final de la coleccion\n"
              "3) Mostrar numero de una posicion\n"
              "0) Salir\n")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            numero = input("Ingrese un numero a insertar: ")
            pos = int(input("Ingrese la posicion en la que se va a insertar: "))
            try:
                coleccion.insertarElemento(numero, pos)
            except ErrorPosicion as e:
                print("El numero {} no pudo ser insertado debido al siguiente error:".format(e.getElemento()))
                print(e.getMensaje())
        elif op == 2:
            numero = int(input("Ingrese un numero a agregar al final: "))
            coleccion.agregarElemento(numero)
        elif op == 3:
            pos = int(input("Ingrese la posicion del numero a mostrar: "))
            try:
                print(coleccion.mostrarElemento(pos))
            except ErrorPosicion as e:
                print("El numero {} no pudo ser mostrado debido al siguiente error:".format(e.getElemento()))
                print(e.getMensaje())
        elif op == 0:
            flag = True
        else:
            print("Opcion no valida")
    
    
    
if __name__ == "__main__":
    c = Coleccion()
    
    Interface(IColeccion(c))