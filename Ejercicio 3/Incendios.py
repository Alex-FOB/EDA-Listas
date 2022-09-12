class Incendios:
    __nombreProvincia = None
    __superficieAfectada = None
    def __init__(self, nom, sup):
        self.__nombreProvincia = nom
        self.__superficieAfectada = sup
    def __str__(self):
        return ("Provincia: {} - Superficie Afectada: {} Hectareas".format(self.__nombreProvincia, self.__superficieAfectada))
    def getNombre(self):
        return self.__nombreProvincia
    def getSup(self):
        return self.__superficieAfectada
    def __gt__(self, other):
        return self.__superficieAfectada < other.getSup()
