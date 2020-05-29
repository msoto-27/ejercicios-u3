class Helado(object):
    __gramos = 0
    __sabores = []
    def __init__(self, gramos, sabores):
        self.__gramos = gramos
        self.__sabores = sabores
    def getGramos(self):
        return self.__gramos
    def getSabores(self):
        return self.__sabores
    def getGramosPorSabor(self, sabor):
        c = 0
        for i in self.__sabores:
            if sabor == i:
                c += self.__gramos / len(self.__sabores)
        return c