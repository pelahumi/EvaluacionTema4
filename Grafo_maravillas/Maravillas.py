class NodoArista():
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None
    
class NodoVertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False 
        self.adyacentes = Arista()


class Arista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0     
        
class Grafo():
    def __init__(self, dirigido= False):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

    def insertar_vertice(self, dato):
        nodo = NodoVertice(dato)
        if self.inicio is None or self.inicio.info > dato:
            nodo.sig = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            act =  self.inicio.info
            while act is not None and act.info < nodo.info:
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        self.tamanio += 1
    