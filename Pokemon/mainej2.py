from pokemon import *

if __name__ == "__main__":
    pokemon = filtrar("Pokemon/pokemon.csv")

    #Parte 1
    arbol_nombres = Arbol()
    agregar(arbol_nombres, "Pokemon/pokemon.csv", "Name")
    arbol_tipos = Arbol()
    agregar(arbol_tipos, "Pokemon/pokemon.csv", "Type 1")
    arbol_id = Arbol()
    agregar(arbol_id, "Pokemon/pokemon.csv", "id")

    #Parte 2
    buscar(arbol_nombres, "Lo que quieres buscar")

    #Parte 3
    pos = buscar_tipos(arbol_tipos, "El tipo que quieras buscar")
    for i in pos:
        print(pokemon["Name"][i])
    
    #Parte 4
    debil = debil_a("Pokemon que quieras")
    print(debil)

    #Parte 5
    
