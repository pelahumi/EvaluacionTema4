import pandas as pd

def filtrar(csv):
    pokemon = pd.read_csv(csv)
    pokemon.rename(columns={"#" : "id"}, inplace=True)
    pokemon = pokemon[["id", "Name", "Type 1"]]
    return pokemon

def agregar(csv, etiqueta, arbol):
    raiz = arbol.raiz.info
    for i in csv[etiqueta]:
        arbol.insertar_nodo(raiz, i)
    return arbol

def buscar(arbol, buscado):
    encontrados = []
    aux = arbol.raiz
    while aux is not None:
        if buscado in aux.info:
            encontrados.append(aux.info)
        aux = aux.sig
    return encontrados

def buscar_tipos(arbol, tipo):
    pos = []
    i = 0
    aux = arbol.raiz
    while aux is not None:
        if tipo == aux.info:
            pos.append(i)
        aux = aux.sig
        i += 1
    return pos

