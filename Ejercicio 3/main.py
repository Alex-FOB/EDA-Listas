from Incendios import Incendios
import csv
from ListaEncPos import ListaEncPos

def CrearObjetos(lista):
    archivo = open("archivo.csv")
    reader = csv.reader(archivo, delimiter=';')
    i = 0
    band = True
    for fila in reader:
        if (band == True):
            band = False
        else:
            prov = fila[3]
            sup = fila[6]
            unIncendio = Incendios(prov, sup)
            lista.insertar(unIncendio, i)
            i += 1

if __name__ == '__main__':
    lista = ListaEncPos()
    CrearObjetos(lista)
    lista.ordenar()
    lista.recorrer()
