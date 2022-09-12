from Nodo import Nodo

class ListaEncPos:
    __primer = None
    __cant = None
    def __init__(self):
        self.__primer = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def primerElemento(self):
        valor = -1
        if(not self.vacia()):
            valor = self.__primer.getDato()
        return valor
    def ultimoElemento(self):
        valor = -1
        if(not self.vacia()):
            aux = self.__primer
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            valor = aux.getDato()
        return valor
    def siguiente(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__primer.getSiguiente()
            else:
                i = 0
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if(i == pos):
                    valor = aux.getSiguiente()
        return valor
    def anterior(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = None
            else:
                i = 1
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if(i == pos):
                    valor = aux
        return valor
    def insertar(self, dato, pos):
        if(self.vacia and pos == 0):
            self.__primer = Nodo(dato)
            self.__cant += 1
        else:
            if(pos == 0):
                nodo = Nodo(dato)
                nodo.setSiguiente(self.__primer)
                self.__primer = nodo
                self.__cant += 1
            else:
                nodo = Nodo(dato)
                anterior = self.anterior(pos)
                if(anterior != -1):
                    siguiente = anterior.getSiguiente()
                    nodo.setSiguiente(siguiente)
                    anterior.setSiguiente(nodo)
                    self.__cant += 1
                else:
                    raise IndexError
    def suprimir(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__primer.getDato()
                self.__primer = self.__primer.getSiguiente()
                self.__cant -= 1
            else:
                anterior = self.anterior(pos)
                if(anterior != -1):
                    siguiente = self.siguiente(pos)
                    if(siguiente != -1):
                        anterior.setSiguiente(siguiente)
                        self.__cant -= 1
                    else:
                        raise IndexError
                else:
                    raise IndexError
        return valor
    def recuperar(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__primer.getDato()
            else:
                i = 0
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                valor = aux.getDato()
        return valor
    def buscar(self, dato):
        pos = -1
        if(not self.vacia()):
            i = 0
            aux = self.__primer
            while aux.getSiguiente() != None and pos == -1:
                if(aux.getDato() == dato):
                    pos = i
                i += 1
                aux = aux.getSiguiente()
        return
    def recorrer(self):
        if(not self.vacia()):
            aux = self.__primer
            while aux.getSiguiente() != None:
                dato = aux.getDato()
                print(dato)
                aux = aux.getSiguiente()
    def ordenar(self):
        band = 1
        cota = self.__cant
        while band != -1:
            band = -1
            i = 0
            aux = self.__primer
            while i < cota:
                siguiente = aux.getSiguiente()
                if (siguiente != None and aux.getDato() > siguiente.getDato()):
                    dato = aux.getDato()
                    aux.setDato(siguiente.getDato())
                    siguiente.setDato(dato)
                    band = i
                aux = aux.getSiguiente()
                i += 1
            cota = band
