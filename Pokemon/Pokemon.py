import pandas as pd

def filtrar(csv):
    pokemon = pd.read_csv(csv)
    pokemon.rename(columns={"#" : "id"}, inplace=True)
    pokemon = pokemon[["id", "Name", "Type 1"]]
    return pokemon