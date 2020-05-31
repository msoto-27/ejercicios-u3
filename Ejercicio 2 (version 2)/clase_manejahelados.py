from clase_helado import Helado

class ManejaHelados(object):
    __helados = []
    def __init__(self):
        self.__helados = []
    def registrarPedido(self, tipo, lista):
        self.__helados.append(Helado(tipo, lista))
    def contarSabores(self, longitud):
        contador = [0 for i in range(longitud)]

        for i in self.__helados:
            for j in i.getSabores():
                n = j.getNumero()
                contador[n-1] += 1
        maximos = [0 for i in range(5)]
        for i in range(len(contador)):
            j = 0
            while j < 5 and i + 1 not in maximos:
                if contador[i] > maximos[j]:
                    maximos.insert(j, i+1)
                    del maximos[5]
                else:
                    j += 1
        ret = [i for i in maximos if i!=0]
        return ret

        
    def estimarTotalGramos(self, sabor):
        c = 0
        for i in self.__helados:
            c += i.getGramosPorSabor(sabor)
        return c
    def mostrarSaboresPorTipo(self, tipo):
        sabores = []
        for i in self.__helados:
            if i.getGramos() == tipo:
                for j in i.getSabores():
                    if j not in sabores:
                        sabores.append(j)
        return sabores