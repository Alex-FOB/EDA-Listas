class Celda:
    __dato = None
    __siguiente = None
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = -1
    def setSiguiente(self, siguiente = -1):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def setDato(self, dato):
        self.__dato = dato
    def getDato(self):
        return self.__dato