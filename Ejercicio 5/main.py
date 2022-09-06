from listaEncadenada import Lista

def inicio():
    contenido = [10, 5, 7, 5, 2, 10]
    lista = Lista()
    i = 0
    for dato in contenido:
        lista.insertar(dato, i)
        i += 1
    return lista
def mostrar(lista):
    contenido = lista.recorrer()
    print(contenido)
if __name__ == '__main__':
    lista = inicio()
    print('Lista inicial:')
    mostrar(lista)
    op = input('Punto A o B: ').lower()
    if(op == 'a'):
        lista.verificarA()
        print('Lista revisada (SIN ORDENAR)')
        mostrar(lista)
    elif(op == 'b'):
        lista.ordenar()
        mostrar(lista)
        lista.verificarB()
        print('Lista revisada (ORDENADA)')
        mostrar(lista)