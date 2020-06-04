class ColeccionPersona(object):
    __personas = []
    def __init__(self):
        self.__personas = []
    def agregarPersona(self, persona):
        self.__personas.append(persona)
    def buscarPorDNI(self, dni):
        i = 0
        while i<len(self.__personas) and self.__personas[i].getDNI() != dni:
            i += 1
        if i<len(self.__personas):
            r = self.__personas[i]
        else:
            r = None
        return r
    