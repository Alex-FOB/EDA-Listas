import numpy as np

from celda import Celda

class Lista:
    __arreglo = None
    __primerL = None #primer elemento de la lista
    __primerD = None #primer espacio disponible
    __cant = None
    def __init__(self, cant = 0):
        self.__arreglo = np.empty(cant, dtype=Celda)
        #luego hay que llenarlas con celdas
        self.incializacion()
        self.__primerL = -1
        self.__primerD = 0
        self.__cant = 0
    def incializacion(self): #llena el arreglo con celdas vacias
        print('ENTRA')
        for i in range(len(self.__arreglo)):
            nodo = Celda(0)
            if(i == 0):
                self.__arreglo[i] = nodo
            else:
                self.__arreglo[i] = nodo
                self.__arreglo[i-1].setSiguiente(i)
    def vacia(self):
        return self.__primerL == -1
    def primerElemento(self):
        return self.__arreglo[self.__primerL].getDato()
    def ultimoElemento(self):
        dato = None
        aux = self.__primerL
        while self.__arreglo[aux].getSiguiente() != -1:
            aux = self.__arreglo[aux].getSiguiente()
        dato = self.__arreglo[aux].getDato()
        return dato
    def siguiente(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__arreglo[self.__primerL].getSiguiente()
            else:
                i = 0
                aux = self.__primerL
                while self.__arreglo[aux].getSiguiente() != -1 and i < pos:
                    i += 1
                    aux = self.__arreglo[aux].getSiguiente()
                if(i == pos):
                    valor = self.__arreglo[aux].getSiguiente()
                    self.__cant += 1
        return valor
    def anterior(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = None
            else:
                i = 1 #para posicionarse un lugar antes
                aux = self.__primerL
                while self.__arreglo[aux].getSiguiente() != -1 and i < pos:
                    i += 1
                    aux = self.__arreglo[aux].getSiguiente()
                if(i == pos):
                    valor = aux
        return valor
    def insertar(self, dato, pos):
        pos -= 1
        if(self.vacia()):
            if(pos == 0):
                nodo = Celda(dato) #se crea el dato 
                self.__primerL = self.__primerD #se copia la posicion del espacio disponible
                self.__primerD = self.__arreglo[self.__primerD].getSiguiente() #se obtiene el siguiente espacio disponible
                self.__arreglo[self.__primerL] = nodo
                self.__cant += 1
        elif(self.__primerD != -1):
            if(pos == 0):
                nodo = Celda(dato)
                nodo.setSiguiente(self.__primerL) #apunta al primer elemento
                aux = self.__primerD #almacenamos el espacio disponible en un dato auxiliar
                self.__primerD = self.__arreglo[self.__primerD].getSiguiente() #apuntamos al siguiente espacio libre
                self.__arreglo[aux] = nodo
                self.__primerL = aux #posicion del nuevo primer elemento
                self.__cant += 1
            else:
                nodo = Celda(dato)
                anterior = self.anterior(pos) #obtiene la posicion anterior
                if(anterior != -1):
                    siguiente = self.__arreglo[anterior].getSiguiente() #obtiene la posicion del siguiente
                    nodo.setSiguiente(siguiente) #el nuevo apunta al siguiente
                    aux = self.__primerD #obtiene el espacio libre
                    self.__primerD = self.__arreglo[self.__primerD].getSiguiente() #apunta al siguiente espacio libre
                    self.__arreglo[anterior].setSiguiente(aux) #el anterior apunta al nuevo
                    self.__arreglo[aux] = nodo
                    self.__cant += 1
                else:
                    raise IndexError
        else:
            raise IndexError('ERROR: lista llena')
    def suprimir(self, pos):
        valor = -1
        if(not self.vacia() and pos > 1 and pos < self.__cant+1): #verifica si no esta vacia y que la posicion sea valida
            pos -= 1
            if(pos == 0):
                aux = self.__primerL
                self.__primerL = self.__arreglo[self.__primerL].getSiguiente()
                self.__arreglo[aux].setSiguiente(self.__primerD)
                self.__primerD = aux
                self.__cant -= 1
            else:
                anterior = self.anterior(pos) #obtenemos la posicion anterior
                if(anterior != -1):
                    aux = self.__arreglo[anterior].getSiguiente() #obtenemos la posicion del elemento
                    siguiente = self.__arreglo[aux].getSiguiente() #obtenemos la posicion del siguiente
                    self.__arreglo[anterior].setSiguiente(siguiente) #une el anterior con el siguiente
                    self.__arreglo[aux].setSiguiente(self.__primerD) #el espacio libre apunta al pimero de la pila libre
                    self.__primerD = aux
                    self.__cant -= 1
                else:
                    raise IndexError
        return valor
    def recuperar(self, pos):
        valor = -1
        if(not self.vacia() and pos > 1 and pos < self.__cant+1):
            pos -= 1
            aux = self.__primerL
            i = 0
            while self.__arreglo[aux].getSiguiente() != -1 and i < pos:
                i += 1
                aux = self.__arreglo[aux].getSiguiente()
            if(i == pos):
                valor = self.__arreglo[aux].getDato()
            else:
                raise IndexError
        return valor
    def buscar(self, dato):
        pos = -1
        if(not self.vacia()):
            band = False
            aux = self.__primerL
            while not band and self.__arreglo[aux].getSiguiente() != -1:
                if(self.__arreglo[aux].getDato() == dato):
                    pos = aux
                    band = True
                aux = self.__arreglo[aux].getSiguiente()
        return pos
    
    def recorrer(self):
        lista = []
        aux = self.__primerL
        while self.__arreglo[aux].getSiguiente() != -1:
            lista.append(self.__arreglo[aux].getDato())
            aux = self.__arreglo[aux].getSiguiente()
        lista.append(self.__arreglo[aux].getDato())
        print('Memoria disponible: ', self.__primerD)
        return lista