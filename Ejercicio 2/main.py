from listaEP import Lista

def init():
    datos = [4, 8, 9, 1, 3]
    lista = Lista(5)
    for i in range(5):
        lista.insertar(datos[i], i+1)
    return lista
if __name__ == '__main__':
    lista = init()
    print(lista.recorrer())
    lista.suprimir(3)
    print(lista.recorrer())
    lista.suprimir(5)
    print(lista.recorrer())