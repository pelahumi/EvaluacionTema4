from Extras.Cola import Cola

class NodoArbol:
    def __init__(self, info, izq=None, der=None):
        self.info = info
        self.izq = izq
        self.der = der

class Arbol():
    def __init__(self, clave):
        self.raiz = NodoArbol(clave)
    
    def insertar_nodo(self, raiz, dato):
        if raiz is None:
            raiz = NodoArbol(dato)
        elif dato < raiz.izq:
            raiz.izq = self.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = self.insertar_nodo(raiz.der, dato)
        return raiz

    def eliminar_nodo(self, raiz, clave):
        x = None
        if raiz is not None:
            if clave < raiz.info:
                raiz.izq, x = self.eliminar_nodo(raiz.izq, clave)
            elif clave > raiz.info:
                raiz.der, x = self.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if raiz.izq is not None:
                    raiz = raiz.der
                elif raiz.der is not None:
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = self.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x

    def arbol_vacio(self, raiz):
        return raiz is None
    
    def remplazar(self, raiz):
        aux = None
        if raiz.der is not None:
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = self.remplazar(raiz.der)
        return raiz, aux
    
    def por_nivel(self, raiz):
        pendientes = Cola()
        pendientes.arribo(raiz)
        while not pendientes.cola_vacia():
            nodo = pendientes.atencion()
            print(nodo.info)
            if nodo.izq is not None:
                pendientes.arribo(nodo.izq)
            if nodo.der is not None:
                pendientes.arribo(nodo.der)

    def inorden(self, raiz):
        if raiz is not None:
            self.inorden(raiz.izq)
            print(raiz.info)
            self.inorden(raiz.der)

    def preorden(self, raiz):
        if raiz is not None:
            print(raiz.info)
            self.preorden(raiz.izq)
            self.preorden(raiz.der)

    
    def postorden(self, raiz):
        if raiz is not None:
            self.postorden(raiz.der)
            print(raiz.info)
            self.postorden(raiz.izq)

    def buscar(self, raiz, clave):
        pos = None
        if raiz is not None:
            if raiz.info == clave:
                pos = raiz
            elif clave < raiz.info:
                self.buscar(raiz.izq, clave)
            else:
                self.buscar(raiz.der, clave)
        return pos