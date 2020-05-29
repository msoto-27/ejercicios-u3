import csv

from clase_sabor import Sabor

class ManejaSabores(object):
    __sabores = []
    def __init__(self):
        file = open('sabores.csv')
        reader = csv.reader(file)
        for line in reader:
            unSabor = Sabor(int(line[0]), line[1], line[2])
            self.__sabores.append(unSabor)        
    def getLongitudLista(self):
        return len(self.__sabores)
    def getSabor(self, numero):
        return self.__sabores[numero]