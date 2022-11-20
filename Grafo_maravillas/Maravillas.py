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


