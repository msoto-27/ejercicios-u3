from menu import Menu

if __name__ == "__main__":
    m = Menu()
    
    salir = False
    while not salir:
        print("===== MENU DE OPCIONES =====\n"
              "1) Insertar un vehiculo en una posicion determinada de la coleccion\n"
              "2) Agregar un vehiculo a la colección\n"
              "3) Mostrar que tipo de vehiculo se encuentra en una determinada posicion\n"
              "4) Modificar el precio de un vehiculo\n"
              "5) Mostrar todos los datos del vehiculo mas economico\n"
              "6) Mostrar resumen de datos de todos los vehiculos\n"
              "7) Guardar la informacion de los vehiculos en un archivo JSON\n"
              "0) Salir\n")
        op = int(input("Ingrese una opcion: "))
        m.opcion(op)
        salir = op == 0