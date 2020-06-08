from menu import Menu

if __name__ == "__main__":
    m = Menu()
    
    salir = False
    while not salir:
        print("===== MENU =====\n"
              "1) Insertar un agente en una determinada posicion\n"
              "2) Agregar un agente\n"
              "3) Mostrar que tipo de agente se encuentra en una posicion determinada de la lista\n"
              "4) Generar listado ordenado por nombre de docentes investigadores de una determinada carrera\n"
              "5) Mostrar cantidad de investigadores y docentes investigadores de una determinada area\n"
              "6) Mostrar listado ordenado por apellido con sueldos de todos los agentes\n"
              "7) Listar datos de docentes investigadores de una determinada categoria y calcular el total de sus importes extra por investigacion y docencia\n"
              "8) Almacenar los datos de todos los agentes en el archivo 'personal.json'\n"
              "0) Salir")
        op = int(input("Ingrese una opcion: "))
        m.opcion(op)
        salir = op == 0
        