class NodoArbol:
    def __init__(self, info, prob, izq=None, der=None):
        self.info = info
        self.prob = prob
        self.izq = izq
        self.der = der


class ListaNodos():
    def __init__(self):
        self.lista = []
    
    def agregar_nodo(self, nodo):
        self.lista.append(nodo)

    def sort(self):
        i = 0
        control = True
        while i <= len(self.lista)-2 and control:
            control = False
            for j in range(0, len(self.lista)-i-1):
                if self.lista[j].prob > self.lista[j+1].prob:
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
                    control = True
        i += 1
        return self.lista
    
    def barrido(self):
        i = 0
        while i < len(self.lista):
            print(self.lista[i].der.izq.izq.prob)
            i += 1
        else:
            return
    def eliminar_nodo(self, clave):
        self.lista.remove(clave)

    def suma(self):
        control = True
        while control:
            control = False
            if len(self.lista) > 1:
                prob = self.lista[0].prob + self.lista[1].prob
                nuevo_nodo = NodoArbol(None, prob, self.lista[0], self.lista[1])
                self.agregar_nodo(nuevo_nodo)
                self.eliminar_nodo(self.lista[0])
                self.eliminar_nodo(self.lista[0])
                self.sort()
                control = True
                


    
        


                
    


