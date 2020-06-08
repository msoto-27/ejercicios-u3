import json

from lista import Lista
from personal_apoyo import PersonalApoyo
from docente import Docente
from investigador import Investigador
from docente_investigador import DocenteInvestigador

class ObjectEncoder(object):
    def cargar(self):
        with open("personal.json", encoding = "UTF-8") as archivo:
            diccionario = json.load(archivo)
            archivo.close()
        return diccionario
    def guardar(self, elementos):
        with open("personal.json", "w", encoding = "UTF-8") as archivo:
            json.dump(elementos, archivo, indent = 4)
            archivo.close()
    def decodificar(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "Lista":
                elementos = d["datos"]
                lista = class_()
                for i in range(len(elementos)):
                    delemento = elementos[i]
                    class_name = delemento.pop("__class__")
                    class_ = eval(class_name)
                    atributos = delemento["__atributos__"]
                    agente = class_(**atributos)
                    lista.agregarElemento(agente)
        return lista
