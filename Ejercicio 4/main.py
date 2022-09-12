import csv
from listaEncadenadaPosicion import ListaEncadenadaPos
from designacion import Designacion


if __name__ == '__main__':
    lista = ListaEncadenadaPos()
    band = False
    archivo = open('estadistica-designacion-magistrados-federal-nacional-por-genero-20220323.csv', encoding='utf8')
    reader = csv.reader(archivo, delimiter=',')
    i = 0
    for fila in reader:
        if not band:
            band = True
        else:
            des = Designacion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            lista.insertar(des, i)
            i += 1
    archivo.close()
    opcion = input('1- Mostrar cantidad de mujeres en un cargo por año\n2 - Mostrar cantidad de agentes por año\n0 - SALIR\nOpcion: ')
    while opcion != '0':
        if opcion == '1':
            cargo = input('Cargo: ')
            print(lista.mujeresPorCargo(cargo))
        elif opcion == '2':
            try:
                materia = input('Materia: ')
                cargo = input('Cargo: ')
                anio = int(input('Año: '))
                if 2000 <= anio <= 2021:
                    print('Cantidad de agentes con cargo "{}" en materia "{}" en el año {}: {}'.format(cargo.lower(), materia.lower(), anio, lista.materiaCargoAnio(materia, cargo, anio)))
                else:
                    raise ValueError
            except ValueError:
                print('ERROR - Ingrese un año válido.')
        else:
            print('ERROR - Ingrese una opción válida.')
        opcion = input('1- Mostrar cantidad de mujeres en un cargo por año\n2 - Mostrar cantidad de agentes por año\n0 - SALIR\nOpcion: ')
