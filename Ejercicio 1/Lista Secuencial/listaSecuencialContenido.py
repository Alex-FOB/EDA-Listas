import numpy as np


class ListaSecuencialCont:
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

    def insertar(self, dato):
        if self.__ultimo != self.__cant - 1:
            if self.__ultimo == -1:
                self.__ultimo += 1
                self.__listaSec[self.__ultimo] = dato
            else:
                actual = self.__ultimo
                band = dato < self.__listaSec[actual]
                if band:
                    while dato < self.__listaSec[actual]:
                        self.__listaSec[actual+1] = self.__listaSec[actual]
                        actual -= 1
                    self.__listaSec[actual+1] = dato
                    self.__ultimo += 1
                else:
                    self.__ultimo += 1
                    self.__listaSec[self.__ultimo] = dato

    def suprimir(self, posicion):
        if posicion == self.__ultimo:
            self.__listaSec[posicion] = 0
            self.__ultimo -= 1
        else:
            self.__listaSec[posicion] = 0    # suprimir y luego desplazar posiciones
            actual = posicion
            while actual < self.__ultimo:
                self.__listaSec[actual] = self.recuperar(actual+1)
                actual += 1
            self.__listaSec[self.__ultimo] = 0
            self.__ultimo -= 1
        print(self.__listaSec)

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
        ult = 0
        if not self.vacia():
            ult = self.recuperar(self.__ultimo)
        return ult

    def primerElemento(self):
        prim = 0
        if not self.vacia():
            prim = self.recuperar(0)
        return prim

    def siguiente(self, posicion):
        sig = 0
        if not self.vacia():
            if self.recuperar(posicion+1) != 0:
                sig = self.recuperar(posicion+1)
            return sig
        else:
            print("Lista Vacia")

    def anterior(self, posicion):
        ant = 0
        if not self.vacia():
            if self.recuperar(posicion-1) != 0:
                ant = self.recuperar(posicion-1)
            return ant
        else:
            print("Lista Vacia")

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__cant):
                elemento = self.recuperar(i)
                print(elemento)
