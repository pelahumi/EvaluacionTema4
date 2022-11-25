from Maravillas import *

def mas_de_una_maravilla(grafo, pais):
    maravillas = []
    aux = grafo.inicio
    while not aux.visitado:
        if aux.pais == pais:
            maravillas.append(aux.nombre)
            aux = aux.sig
        else:
            aux = aux.sig
    if len(maravillas) > 1:
        return True
    else:
        return False

