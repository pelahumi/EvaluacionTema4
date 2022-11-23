class NodoCola():
    def __init__(self, info, sig=None):
        self.info = info
        self.sig = sig

class Cola():
    def  __init__(self, frente=None, final=None):
        self.frente = NodoCola(frente)
        self.final = NodoCola(final)
        self.tamanio = 0
    
    def arribo(self, dato):
        nodo = NodoCola(dato)
        if self.tamanio == 0:
            self.frente = nodo
        else:
            self.final.sig = nodo
        self.final = nodo
        self.tamanio += 1

    def atencion(self):
        dato = self.frente
        self.frente = self.frente.sig
        self.tamanio -= 1
        return dato.info
    
    def cola_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False
    
    def en_frente(self):
        return self.frente.info
    
    def tamanio(self):
        return self.tamanio

    def mover_al_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato

    def barrido(self):
        i = 0
        while i < self.tamanio:
            dato = self.mover_al_final()
            print(dato)
            i += 1