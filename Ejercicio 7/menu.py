from object_encoder import ObjectEncoder
from lista import Lista
from personal_apoyo import PersonalApoyo
from docente import Docente
from investigador import Investigador
from docente_investigador import DocenteInvestigador

class Menu(object):
    __switcher = dict
    __lista = None
    def __init__(self):
        self.__switcher = {1:self.opcion1, 2:self.opcion2, 3:self.opcion3, 4:self.opcion4, 5:self.opcion5, 6:self.opcion6, 7:self.opcion7, 8:self.opcion8, 0:self.salir}
        obj = ObjectEncoder()
        self.__lista = obj.decodificar(obj.cargar())

        
    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func()
    def salir(self):
        print("Fin del programa")
    def crearAgente(self):
        cuil = input("Ingrese cuil: ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        basico = float(input("Ingrese sueldo basico: "))
        antiguedad = int(input("Ingrese antiguedad: "))
        
        categoria = 0
        carrera = ''
        cargo = ''
        catedra = ''
        area = ''
        tipo_i = ''
        extra = ''
        tipo = ''
        while tipo not in ["PA", "D", "I", "DI"]:
            tipo = input("Ingrese el tipo de agente ('PA' = Personal de Apoyo | 'D' = Docente | 'I' = Investigador | 'DI' = Docente Investigador) : ").upper()
        if tipo == "PA":
            
            while not (1 <= categoria <= 22):
                categoria = int(input("Ingrese una categoria (1-22): "))
        else:
            if "D" in tipo:
                carrera = input("Ingrese la carrera: ")
                while cargo not in ["simple", "semi-exclusivo", "exclusivo"]:
                    cargo = input("Ingrese el cargo (simple, semi-exclusivo o exclusivo) : ").lower()
                catedra = input("Ingrese la catedra: ")
            if "I" in tipo:
                area = input("Ingrese el area de investigacion: ")
                tipo_i = input("Ingrese el tipo de investigacion: ")
            if tipo == "DI":
                while categoria not in ["I", "II", "III", "IV", "V"]:
                    categoria = input("Ingrese la categoria de investigacion (I, II, III, IV, V) : ").upper()
                extra = float(input("Ingrese el importe extra por docencia e investigacion: "))
        d = {
            "PA":PersonalApoyo(cuil, nombre, apellido, basico, antiguedad, categoria),
            "D":Docente(cuil, nombre, apellido, basico, antiguedad, carrera, cargo, catedra),
            "I":Investigador(cuil, nombre, apellido, basico, antiguedad, area, tipo_i),
            "DI":DocenteInvestigador(cuil, nombre, apellido, basico, antiguedad, carrera, cargo, catedra, area, tipo_i, categoria, extra)
            }
        agente = d[tipo]
        return agente
    
    def opcion1(self):
        agente = self.crearAgente()
        pos = int(input("Ingrese la posicion en la lista en la que se insertará el agente: "))
        self.__lista.insertarElemento(agente, pos-1)
    def opcion2(self):
        agente = self.crearAgente()
        self.__lista.agregarElemento(agente)
        print("Agente agregado")
    def opcion3(self):
        pos = int(input("Ingrese la posicion del agente a mostrar: "))
        try:
            agente = self.__lista.mostrarElemento(pos-1)
        except IndexError:
            print("Posicion fuera de rango")
        else:
            d = {PersonalApoyo:"Personal de Apoyo", Docente:"Docente", Investigador:"Investigador", DocenteInvestigador:"Docente Investigador"}
            print("El agente en la posicion seleccionada es del tipo:", d[agente.__class__])
    def opcion4(self):
        carrera = input("Ingrese una carrera: ")
        lista_aux = self.__lista.listadoCarrera(carrera)
        print("Mostrando listado de todos los docentes investigadores de la carrera seleccionada:")
        for i in lista_aux:
            print(i)
    def opcion5(self):
        area = input("Ingrese un area de investigacion: ")
        inv, docinv = self.__lista.contarInvestigadores(area)
        print("El area seleccionada cuenta con:\nInvestigadores: {}\nDocentes Investigadores: {}".format(inv, docinv))
    def opcion6(self):
        print("Mostrando datos de agentes:")
        self.__lista.mostrarSueldos()
    def opcion7(self):
        categoria = None
        while categoria not in ["I", "II", "III", "IV", "V"]:
            categoria = input("Ingrese una categoria de investigacion (I, II, III, IV, V) : ").upper()
        print("La suma que debe de ser solicitada en concepto de importes extra en por investigacion y docencia en la categoria seleccionada es de: $", self.__lista.listadoCategoria(categoria))
    def opcion8(self):
        obj = ObjectEncoder()
        obj.guardar(self.__lista.toJSON())
        print("Los datos han sido guardados")
        