class Designacion:
    __anio = 0
    __fedONac = None
    __tipoCargo = None
    __tipoInstancia = None
    __materia = None
    __cantVarones = None
    __cantMujeres = None

    def __init__(self, anio, fedONac, tipoCargo, tipoInst, materia, varones, mujeres):
        self.__anio = anio
        self.__fedONac = fedONac
        self.__tipoCargo = tipoCargo
        self.__tipoInstancia = tipoInst
        self.__materia = materia
        self.__cantVarones = varones
        self.__cantMujeres = mujeres

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.__anio, self.__fedONac, self.__tipoCargo, self.__tipoInstancia, self.__materia, self.__cantVarones, self.__cantMujeres)

    def getVarones(self):
        return self.__cantVarones

    def getMujeres(self):
        return self.__cantMujeres

    def getAnio(self):
        return self.__anio

    def getCargo(self):
        return self.__tipoCargo

    def getMateria(self):
        return self.__materia
