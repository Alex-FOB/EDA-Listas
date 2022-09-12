from celda import Celda


class ListaEncadenadaPos:
    __primer = None
    __cant = None

    def __init__(self):
        self.__primer = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def primerElemento(self):
        valor = -1
        if not self.vacia():
            valor = self.__primer.getDato()
        return valor

    def ultimoElemento(self):
        valor = -1
        if not self.vacia():
            aux = self.__primer
            while aux.getSiguiente() is not None: # recorre hasta el final
                aux = aux.getSiguiente()
            valor = aux.getDato()
        return valor

    def siguiente(self, pos):
        valor = -1
        if not self.vacia():
            if pos == 0:
                valor = self.__primer.getSiguiente()
            else:
                i = 0  # para que se coloque en la posición deseada
                aux = self.__primer
                while aux.getSiguiente() is not None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if i == pos:
                    valor = aux.getSiguiente() # retorna el siguiente
        return valor

    def anterior(self, pos):
        valor = -1
        if not self.vacia():
            if pos == 0:
                valor = None
            else:
                i = 1 # para que se coloque en la posición anterior deseada
                aux = self.__primer
                while aux.getSiguiente() is not None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if i == pos:
                    valor = aux  # retorna el anterior
        return valor

    def insertar(self, dato, pos):  # MODIFICAR
        if self.vacia and pos == 0:
            self.__primer = Celda(dato)
            self.__cant += 1
        else:
            if pos == 0:
                nodo = Celda(dato)
                nodo.setSiguiente(self.__primer)
                self.__primer = nodo
                self.__cant += 1
            else:
                nodo = Celda(dato)
                anterior = self.anterior(pos)
                if anterior != -1:
                    siguiente = anterior.getSiguiente()
                    nodo.setSiguiente(siguiente)
                    anterior.setSiguiente(nodo)
                    self.__cant += 1
                else:
                    raise IndexError

    def suprimir(self, pos):  # MODIFICAR
        valor = -1
        if not self.vacia():
            if pos == 0:
                valor = self.__primer.getDato()
                self.__primer = self.__primer.getSiguiente()
                self.__cant -= 1
            else:
                anterior = self.anterior(pos)
                if anterior != -1:
                    siguiente = self.siguiente(pos)
                    if siguiente != -1:
                        anterior.setSiguiente(siguiente)
                        self.__cant -= 1
                    else:
                        raise IndexError
                else:
                    raise IndexError
        return valor

    def recuperar(self, pos):
        valor = -1
        if not self.vacia():
            if pos == 0:
                valor = self.__primer.getDato()
            else:
                i = 0
                aux = self.__primer
                while aux.getSiguiente() is not None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                valor = aux.getDato()
        return valor

    def buscar(self, dato):
        pos = -1
        if not self.vacia():
            i = 0
            aux = self.__primer
            while aux.getSiguiente() is not None and pos == -1:
                if aux.getDato() == dato:
                    pos = i
                i += 1
                aux = aux.getSiguiente()
        return pos

    def recorrer(self):
        if not self.vacia():
            aux = self.__primer
            while aux is not None:
                print(aux.getDato())
                aux = aux.getSiguiente()

    def mujeresPorCargo(self, cargo):
        if not self.vacia():
            aux = self.__primer
            cant = 0
            anio = 2000
            text = ''
            while aux is not None:
                dato = aux.getDato()
                anioAux = int(dato.getAnio())
                if anio == anioAux:
                    if cargo.lower() == dato.getCargo().lower():
                        cant += int(dato.getMujeres())
                else:
                    text += 'Año {}: {} mujeres en el cargo de "{}".\n'.format(anio, cant, cargo.lower())
                    anio += 1
                    cant = 0
                    if cargo.lower() == dato.getCargo().lower():
                        cant += int(dato.getMujeres())
                if aux.getSiguiente() is None:
                    text += 'Año {}: {} mujeres en el cargo de "{}".\n'.format(anio, cant, cargo.lower())
                aux = aux.getSiguiente()
            return text

    def materiaCargoAnio(self, materia, cargo, anio):
        aux = self.__primer
        cant = 0
        band = False
        while not band:
            dato = aux.getDato()
            anioAux = dato.getAnio()
            if anioAux == anio:
                if (materia == dato.getMateria()) and (cargo == dato.getCargo()):
                    cant += 1
            elif anioAux == anio + 1:
                band = True
            aux = aux.getSiguiente()
        return cant
