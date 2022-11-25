from Maravillas import *

if __name__ == "__main__":
    #Vertices
    maravillas_naturales = Grafo()
    maravillas_naturales.insertar_vertice(1, "Amazonas", "Brasil", "Naturales")
    maravillas_naturales.insertar_vertice(2, "Bahia de Ha Long", "Vietnam", "Naturales")
    maravillas_naturales.insertar_vertice(3, "Cataratas del Iguazu", "Argentina", "Naturales")
    maravillas_naturales.insertar_vertice(4, "Jeju", "Corea del Sur", "Naturales")
    maravillas_naturales.insertar_vertice(5, "Komodo", "Indonesia", "Naturales")
    maravillas_naturales.insertar_vertice(6, "Cataratas del Niagara", "Canada", "Naturales")
    maravillas_naturales.insertar_vertice(7, "Montaña de la Mesa", "Ciudad del Cabo", "Naturales")

    maravillas_arquitectonicas = Grafo()
    maravillas_arquitectonicas.insertar_vertice(1, "Chichen Itza", "Mexico", "Arquitectonica")
    maravillas_arquitectonicas.insertar_vertice(2, "Cristo Redentor", "Brasil", "Arquitectonica")
    maravillas_arquitectonicas.insertar_vertice(3, "Coliseo Romano", "Italia", "Arquitectonica")
    maravillas_arquitectonicas.insertar_vertice(4, "Gran Muralla China", "China", "Arquitectonica")
    maravillas_arquitectonicas.insertar_vertice(5, "Machu Picchu", "Peru", "Arquitectonica")
    maravillas_arquitectonicas.insertar_vertice(6, "Petra", "Jordania", "Arquitectonica")
    maravillas_arquitectonicas.insertar_vertice(7, "Taj Mahal", "India", "Arquitectonica")

    #Aristas
    maravillas_naturales.agregar_arista()
