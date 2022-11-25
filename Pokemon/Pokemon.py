import pandas as pd
from Arbol import *

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

def debilidades(tipo):
    debilidades = []
    if tipo == "Normal":
        debilidades.append("Fight")
    elif tipo == "Fighting":
        debilidades.append("Flying")
        debilidades.append("Psychic")
        debilidades.append("Fairy")
    elif tipo == "Flying":
        debilidades.append("Rock")
        debilidades.append("Electric")
        debilidades.append("Ice")
    elif tipo == "Poisson":
        debilidades.append("Psychic")
        debilidades.append("Ground")
    elif tipo == "Ground":
        debilidades.append("Water")
        debilidades.append("Ice")
        debilidades.append("Grass")
    elif tipo == "Rock":
        debilidades.append("Water")
        debilidades.append("Grass")
        debilidades.append("Ground")
        debilidades.append("Fight")
        debilidades.append("Steel")
    elif tipo == "Bug":
        debilidades.append("Flying")
        debilidades.append("Rock")
        debilidades.append("Fire")
    elif tipo == "Ghost":
        debilidades.append("Ghost")
        debilidades.append("Dark")
    elif tipo == "Steel":
        debilidades.append("Fight")
        debilidades.append("Ground")
        debilidades.append("Fire")
    elif tipo == "Fire":
        debilidades.append("Ground")
        debilidades.append("Rock")
        debilidades.append("Water")
    elif tipo == "Water":
        debilidades.append("Grass")
        debilidades.append("Electric")
    elif tipo == "Grass":
        debilidades.append("Flying")
        debilidades.append("Poisson")
        debilidades.append("Bug")
        debilidades.append("Fire")
        debilidades.append("Ice")
    elif tipo == "Electric":
        debilidades.append("Ground")
    elif tipo == "Pyschic":
        debilidades.append("Bug")
        debilidades.append("Ghost")
        debilidades.append("Dark")
    elif tipo == "Ice":
        debilidades.append("Fight")
        debilidades.append("Rock")
        debilidades.append("Steel")
        debilidades.append("Fire")
    elif tipo == "Dragon":
        debilidades.append("Dragon")
        debilidades.append("Ice")
        debilidades.append("Fairy")
    elif tipo == "Dark":
        debilidades.append("Fight")
        debilidades.append("Bug")
        debilidades.append("Fairy")
    elif tipo == "Fairy":
        debilidades.append("Poisson")
        debilidades.append("Steel")
    else:
        print("No se encontro el tipo")
    return debilidades

def debil_a(pokemon):
    debil = []
    pokedex = filtrar("Pokemon/pokemon.csv")
    for i in pokedex["Name"]:
        if pokemon == pokedex["Name"][i]:
            tipo = pokedex["Type 1"][i]
    debilidades = debilidades(tipo)
    for i in pokedex["Type 1"]:
        for j in debilidades:
            if i == j:
                debil.append(pokedex["Name"][i])
    return debil

def tipos(arbol):
    tipos = []
    aux = arbol.raiz
    while aux is not None:
        if aux.info not in tipos:
            tipos.append(aux.info)
            aux = aux.sig
        else:
            aux = aux.sig
    return tipos

def cuantos_pokemon_por_tipo(arbol, tipo):
    n = 0
    aux = arbol.raiz
    while aux is not None:
        if tipo == aux.info:
            n += 1
            aux = aux.sig
        else:
            aux.sig
    return n

        

