from celda import Celda

class Lista:
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
            while aux.getSiguiente() != None: #recorre hasta el final
                aux = aux.getSiguiente()
            valor = aux.getDato()
        return valor
    def siguiente(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__primer.getSiguiente()
            else:
                i = 0 #para que se coloque en la posición deseada
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if(i == pos):
                    valor = aux.getSiguiente() #retorna el siguiente
        return valor
    def anterior(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = None
            else:
                i = 1 #para que se coloque en la posición anterior deseada
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if(i == pos):
                    valor = aux #retorna el anterior
        return valor
    def insertar(self, dato, pos): #MODIFICAR
        if(self.vacia and pos == 0):
            self.__primer = Celda(dato)
            self.__cant += 1
        else:
            if(pos == 0):
                nodo = Celda(dato)
                nodo.setSiguiente(self.__primer)
                self.__primer = nodo
                self.__cant += 1
            else:
                nodo = Celda(dato)
                anterior = self.anterior(pos)
                if(anterior != -1):
                    siguiente = anterior.getSiguiente()
                    nodo.setSiguiente(siguiente)
                    anterior.setSiguiente(nodo)
                    self.__cant += 1
                else:
                    raise IndexError
    def suprimir(self, pos): #MODIFICAR
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
        return pos


    def verificarA(self): #punto 5.a
        if(not self.vacia()):
            aux1 = self.__primer
            i = 0
            j = 1
            while aux1.getSiguiente() != None:
                aux2 = aux1.getSiguiente()
                while aux2 != None:
                    if(aux2 != None and aux2.getDato() == aux1.getDato()):
                        self.suprimir(j)
                    j += 1
                    aux2 = aux2.getSiguiente()
                i += 1
                j = i + 1
                aux1 = aux1.getSiguiente()
    def verificarB(self): #punto 5.b
        if(not self.vacia()):
            ant = self.__primer
            aux = self.__primer.getSiguiente()
            i = 1
            cant = self.__cant
            if(aux != None):
                while aux != None:
                    if(aux.getDato() == ant.getDato()):
                        self.suprimir(i)
                        i -= 1
                    else:
                        ant = aux
                    i += 1
                    aux = aux.getSiguiente()
    def recorrer(self):
        lista = []
        if(not self.vacia()):
            i = 0
            j = self.__cant
            aux = self.__primer
            while i < j:
                lista.append(aux.getDato())
                aux = aux.getSiguiente()
                i += 1
        return lista
    def ordenar(self): #Metodo de burbuja mejorado
        band = 1
        cota = self.__cant
        while band != -1:
            band = -1
            i = 0
            aux = self.__primer
            while i < cota:
                siguiente = aux.getSiguiente()
                if(siguiente != None and aux.getDato() > siguiente.getDato()):
                    dato = aux.getDato()
                    aux.setDato(siguiente.getDato())
                    siguiente.setDato(dato)
                    band = i
                aux = aux.getSiguiente()
                i += 1
            cota = band