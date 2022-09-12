import numpy as np
# []


class ListaSecuencial:
    __ultimo = -1
    __cant = 0
    __listaSec = None

    def __init__(self, cantidad=0):
        self.__ultimo = -1
        self.__cant = cantidad
    
    def vacia(self):
        return self.__ultimo == -1

    def crear(self):
        self.__listaSec = np.empty(self.__cant, dtype=int)
        for i in range(self.__cant):
            self.__listaSec[i] = 0

    def recuperar(self, posicion):
        return self.__listaSec[posicion]

    def insertar(self, posicion, dato):
        if self.__ultimo != self.__cant - 1:
            if (posicion >= 0) and (posicion < self.__cant):
                if posicion == self.__ultimo + 1:
                    self.__listaSec[posicion] = dato
                    self.__ultimo += 1
                elif posicion < self.__ultimo:
                    actual = self.__ultimo
                    while actual >= posicion:
                        self.__listaSec[actual + 1] = self.recuperar(actual)
                        actual -= 1
                    self.__listaSec[posicion] = dato
                    self.__ultimo += 1
        self.recorrer()
    

        #if (posicion == self.__ultimo + 1) and (posicion < self.__cant -1):
         #   self.__listaSec[posicion] = dato
         #   self.__ultimo += 1
        #elif (posicion > 0) and (posicion <= self.__ultimo):
         #   if self.acceder(posicion) is None:
          #      self.__listaSec[posicion] = dato
          #  else:
           #     pass    #   desplazar posiciones e insertar


    def suprimir(self, posicion):
        if posicion == self.__ultimo:
            self.__listaSec[posicion] = 0
            self.__ultimo -= 1
        else:
            self.__listaSec[posicion] = 0    #   suprimir y luego desplazar posiciones
            actual = posicion
            while actual < self.__ultimo:
                self.__listaSec[actual] = self.recuperar(actual+1)
                actual += 1
            self.__listaSec[self.__ultimo] = 0
            self.__ultimo -= 1
        self.recorrer()

    def buscar(self, dato):
        i = 0
        band = False
        while (i <= self.__ultimo) and (not band):
            if dato == self.recuperar(i):
                band = True
            else:
                i += 1
        return i
    
    def ultimoElemento(self):
        if not self.vacia():
            return self.__arreglo[self.__ultimo]
        else:
            return None

    def primerElemento(self):
        if not self.vacia():
            return self.__arreglo[0]
        else:
            return None

    def siguiente(self, posicion):
        if not self.vacia():
            if self.recuperar[posicion+1] is not None:
                return self.recuperar[posicion+1]
            else:
                print("No se encontro elemento")
        else:
            print("Lista Vacia")
            
    def anterior(self, posicion):
        if not self.vacia():
            if self.recuperar[posicion-1] is not None:
                return self.recuperar[posicion-1]
            else:
                print("No se encontro elemento")
        else:
            print("Lista Vacia")

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__cant):
                elemento = self.recuperar(i)
                print(elemento)