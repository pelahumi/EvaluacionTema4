class NodoPila():
    def __init__(self, info, sig=None):
        self.info = info
        self.sig = sig

class Pila():
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        self.cima = NodoPila(dato, self.cima)
        self.tamanio +=1

    def desapilar(self):
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x

    def tamanio(self):
        return self.tamanio
    
    def pila_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False
    
    def en_cima(self):
        if self.cima is not None:
            return self.cima.info
        else:
            return None
    
    def barrido(self):
        pila_aux = Pila()
        while (not self.pila_vacia()):
            dato = self.desapilar()
            print(dato)
            pila_aux.apilar(dato)
        while (not pila_aux.pila_vacia()):
            dato = pila_aux.desapilar()
            self.apilar(dato)