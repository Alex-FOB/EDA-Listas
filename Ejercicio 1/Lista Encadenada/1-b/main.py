from listaEncadenada import Lista

def init():
    lista = Lista()
    contenido = [2, 3, 4, 5, 1, 7, 6]
    for dato in contenido:
        lista.insertar(dato)
    return lista
if __name__ == '__main__':
    lista = init()
    print('LISTA: ')
    lista.recorrer()
    print('BORRAR ELMENTO: 4')
    lista.suprimir(4)
    lista.recorrer()
    print('BORRAR ELEMENTO: 1')
    lista.suprimir(1)
    lista.recorrer()
    print('BORRAR ELEMENTO: 7')
    lista.suprimir(7)
    lista.recorrer()