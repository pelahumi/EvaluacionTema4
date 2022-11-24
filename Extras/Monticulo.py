class Monticulo():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio
    
    def flotar(self, indice):
        while indice > 0 and self.vector[indice] > self.vector[(indice - 1)//2]:
            padre = (indice - 1) // 2
            self.intercambio(self.vector, indice, padre)
    
    def agregar(self, dato):
        self.vector[self.tamanio] - dato
        self.flotar(self.tamanio)
