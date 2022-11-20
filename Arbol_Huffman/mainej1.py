from Huffman import *

nodo1 = NodoArbol("A", 0.2)
nodo2 = NodoArbol("F", 0.17)
nodo3 = NodoArbol("1", 0.13)
nodo4 = NodoArbol("3", 0.21)
nodo5 = NodoArbol("0", 0.05)
nodo6 = NodoArbol("M", 0.09)
nodo7 = NodoArbol("T", 0.15)

lista = Huffman()

lista.agregar_nodo(nodo1)
lista.agregar_nodo(nodo2)
lista.agregar_nodo(nodo3)
lista.agregar_nodo(nodo4)
lista.agregar_nodo(nodo5)
lista.agregar_nodo(nodo6)
lista.agregar_nodo(nodo7)

lista.sort()

lista.suma()

print(lista.letra("11100101100", lista.suma()))

