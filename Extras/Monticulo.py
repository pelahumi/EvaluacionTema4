class Monticulo():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio
    
    def flotar(self, indice):
        while indice > 0 and self.vector[indice] > self.vector[(indice - 1)//2]:
            padre = (indice - 1) // 2
            self.intercambio(self.vector, indice, padre)
            indice = padre
    
    def hundir(self, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while control and hijo_izq < self.tamanio:
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if hijo_der < self.tamanio:
                if self.vector[hijo_der] > self.vector[hijo_izq]:
                    aux = hijo_der
            elif self.vector[indice] < self.vector[aux]:
                self.intercambio(indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False
    
    def agregar(self, dato):
        self.vector[self.tamanio] - dato
        self.flotar(self.tamanio)
        self.tamanio += 1

    def quitar(self):
        self.intercambio(0, self.tamanio-1)
        dato = self.vector[self.tamanio-1]
        self.tamanio -= 1
        self.hundir(0)
        return dato
    
    def intercambio(self, indice, padre):
        self.vector[indice], self.vector[padre] = self.vector[padre], self.vector[indice]

    def cantidad_elementos(self):
        return self.tamanio

    def monticulo_vacio(self):
        return self.tamanio == 0
    
    