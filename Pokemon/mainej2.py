from Arbol import *
from pokemon import filtrar

if __name__ == "__main__":
    pokemon = filtrar("Pokemon/pokemon.csv")

    arbol_nombres = Arbol()
    arbol_tipos = Arbol()
    arbol_id = Arbol()

    
