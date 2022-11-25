from Maravillas import *

def mas_de_una_maravilla(grafo, pais):
    maravillas = []
    aux = grafo.inicio
    while aux is not None:
        if aux.pais == pais:
            maravillas.append(aux.nombre)
            aux = aux.sig
        else:
            aux = aux.sig
    if len(maravillas) > 1:
        return True
    else:
        return False

def arquitectonicas_y_naturales(grafo1, grafo2):
    diccionario = {}
    aux1 = grafo1.inicio
    aux2 = grafo2.inicio
    while aux1 is not None and aux2 is not None:
        if aux1.pais == aux2.pais:
            diccionario[aux1.pais] = [aux1.nombre, aux2.nombre]
            aux1 = aux1.sig
            aux2 = aux2.sig
        else:
            aux1 = aux1.sig
            aux2 = aux2.sig
    return diccionario
    
