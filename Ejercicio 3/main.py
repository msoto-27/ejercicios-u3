from clase_menu import Menu

if __name__ == "__main__":
    m = Menu()
    salir = False
    while not salir:
        print("===== MENU DE OPCIONES =====\n"
              "1) Registrar a una persona a un taller\n"
              "2) Consultar datos de inscripcion de una persona\n"
              "3) Mostrar datos de alumnos inscriptos a un taller\n"
              "4) Registrar el pago de la inscripcion a un taller\n"
              "5) Generar un archivo con informacion referente a las inscripciones\n"
              "0) Salir\n")
        op = int(input("Ingrese una opcion: "))
        m.opcion(op)
        salir = op == 0