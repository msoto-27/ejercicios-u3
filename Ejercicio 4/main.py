from menu import Menu

if __name__ == '__main__':
    m = Menu()
    salir = False
    while not salir:
        print("===== MENU DE OPCIONES =====\n"
              "1) Registrar horas de un empleado contratado\n"
              "2) Mostrar el costo total de una de las tareas no finalizadas hasta el dia de hoy\n"
              "3) Mostrar los datos de aquellos empleados que recibiran el plan de ayuda solidaria (empleados con sueldo menor a $25000)\n"
              "4) Mostrar los datos de todos los empleados junto con sus sueldos\n"
              "0) Salir")
        op = int(input("Ingrese una opcion: "))
        m.opcion(op)
        salir = op == 0